from bank import BankManagementSystem, BankAccounts
from ui_func import get_a_prompt_loop


def show_menu(menu):
    print('\n-------------------------------')
    for key in menu:
        print(f"{key}. {menu[key]}")
    print('-------------------------------\n')


def user_select_from_menu(menu):
    show_menu(menu)
    while True:
        user_choice = input("Enter Choice >>> ")
        if user_choice not in menu:
            print(f'{user_choice} not in this menu, try again')
        else:
            return user_choice


main_menu = {"1": "Create a New Bank Account",
             "2": "Deposit Money",
             "3": "withdraw Money",
             "4": "Check Balance",
             "5": "Close your Bank Account",
             "0": "Quit"}

bm = BankManagementSystem('db.db')

while True:
    choice = user_select_from_menu(main_menu)

    if choice == '0':
        break

    elif choice == '1':
        account_holder_name = get_a_prompt_loop("Please enter your full name: ", 2)
        account_email = get_a_prompt_loop("Please enter your email: ", 4)
        account_address = get_a_prompt_loop("Please enter your address: ", 2)
        account_phone_number = get_a_prompt_loop("Please enter your phone num: ", 3)
        account_birth_date = get_a_prompt_loop("Please enter your birth date (YYYY-MM-DD):", 5)
        ba = BankAccounts('db.db', account_holder_name, account_email, account_address, account_phone_number,
                          account_birth_date)
        bm.add_new_account(ba.account_number)
        print(str(ba))

    elif choice in ('2', '3', '4', '5'):
        account_number = get_a_prompt_loop("What is your account number? ", 0)
        account_pin_code = get_a_prompt_loop("Enter your PIN Code for validation: ", 0)
        if bm.account_lookup(account_number, account_pin_code):
            if choice == '2':
                amount = get_a_prompt_loop("Enter the amount you would like to deposit: ", 1)
                if bm.deposit(account_number, account_pin_code, amount):
                    print(f"you have successfully deposited {amount} into your account")
                else:
                    print("The action couldn't be completed.")
            elif choice == '3':
                amount = get_a_prompt_loop("Enter the amount you would like to withdraw: ", 1)
                if bm.withdraw(account_number, account_pin_code, amount):
                    print(f"you have successfully withdrawn {amount} from your account")
                else:
                    print("You don't have enough money to withdraw.")
            elif choice == '4':
                if bm.get_account_balance(account_number, account_pin_code):
                    print("Your Current Balance is: ", bm.get_account_balance(account_number, account_pin_code))
                else:
                    print("You don't have money...")
            elif choice == '5':
                if bm.delete_account(account_number, account_pin_code):
                    print("Your account was deleted.")
                else:
                    print("The action couldn't be completed.")
        else:
            print("Your account number or PIN code are not correct, please try again.")

print("Bye")
