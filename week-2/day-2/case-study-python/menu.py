'''
Responsible for displaying system menu.
'''


class Menu:

    def display_user_menu(self) -> None:
        print('''
            \n --- User Menu --- : 
            1. Display Balance
            2. Transfer
            3. Withdraw
            4. Deposit
            5. Exit
        ''')

    def display_main_menu(self) -> None:
        print('''
            \n --- Main Menu ---
            1. Admin
            2. User
            3. Exit
        ''')

    def display_admin_menu(self) -> None:
        print('''
            \n --- Admin Menu --- 
            1. Create Account
            2. Display Balance
            2. Transfer
            3. Withdraw
            4. Deposit
            5. Status
            6. Exit
        ''')

    def cli_input(self, which: int) -> int:
        if which == 1:
            self.display_main_menu()
        elif which == 2:
            self.display_admin_menu()
        else:
            self.display_user_menu()

        try:
            ch: int = int(input('Enter Your Choice : '))
        except:
            ch = 0
        return ch

    def cli(self) -> None:
        while True:
            ch: int = self.cli_input(1)

            if(ch == 1):
                ch: int = self.cli_input(2)
                if(ch == 6):
                    continue
            elif (ch == 2):
                ch: int = self.cli_input(3)
                if(ch == 5):
                    continue
            elif ch == 0:
                print('\n Please Enter Numbers only')
            else:
                exit(0)
