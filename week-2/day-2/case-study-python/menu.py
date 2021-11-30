'''
Responsible for displaying system menu.
'''
from users import UserDatabase


class Menu:

    def __init__(self) -> None:
        self.udb = UserDatabase()

    def display_main_menu(self) -> None:
        print('''
        \n --- Main Menu ---
        1. Admin
        2. User
        3. Exit
        ''')

    def display_user_menu(self) -> None:
        print('''
        \n --- User Menu --- :
        1. Display Balance
        2. Transfer
        3. Withdraw
        4. Deposit
        5. Back
        ''')

    def display_admin_menu(self) -> None:
        print('''
        \n --- Admin Menu ---
        1. Create Account
        2. Display Balance
        3. Transfer
        4. Withdraw
        5. Deposit
        6. Status
        7. Back
        ''')

    def display_status_sub_menu(self) -> None:
        print('''
        \n --- Manage Account Status ---
        1. Activate
        2. De-Activate
        3. Back
        ''')

    def cli_input(self, which: int) -> int:
        if which == 1:
            self.display_main_menu()
        elif which == 2:
            self.display_admin_menu()
        elif which == 3:
            self.display_user_menu()
        else:
            self.display_status_sub_menu()

        try:
            ch: int = int(input('Enter Your Choice : '))
        except:
            ch = 0
        return ch

    def cli_input_admin(self) -> None:
        ch: int = self.cli_input(2)
        if(ch == 7):
            return
        elif(ch == 6):
            self.cli_input_status()

    def cli_input_user(self) -> None:
        ch: int = self.cli_input(3)
        if(ch == 5):
            return

    def cli_input_status(self) -> None:
        ch: int = self.cli_input(4)
        if(ch == 3):
            self.cli_input(2)

    def cli(self) -> None:
        while True:
            ch: int = self.cli_input(1)
            if(ch == 1):
                self.admin_authentication()
            elif (ch == 2):
                self.cli_input_user()
            elif ch == 0:
                print('\n Please Enter Numbers only')
            else:
                exit(0)

    def admin_authentication(self) -> bool:
        user_name = input('User Name : ')
        password = input('Password : ')
        if(self.udb.check_user_credentials(user_name=user_name, password=password, role='admin')):
            self.cli_input_admin()
        else:
            print('Un Authorized User')
