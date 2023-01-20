import time as t
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

num_of_tries = 5
accounts = []
account_position = None 

with open("account.txt", "r") as f:
    for line in f:
        pin, balance, name = ', '.join(line.strip().split('\n')).split(', ')
        account = {
            "pin": int(pin),
            "balance": float(balance),
            "name": name
        }
        accounts.append(account)

while (num_of_tries != 0):
    print(" *********************************************************** ")
    print(" *                                                         * ")
    print(" *                          ATM                            * ")
    print(" *                                                         * ")
    print(" *********************************************************** ")
    print("\tPlease log-in your account using 4 PIN")
    input_pin = int(input("Login: "))
    account = None
    i = 0
    clear_console()

    for a in accounts:
        if a["pin"] == input_pin:
            account = a
            account_position = i
            break
        i += 1

    if account:
        print(" ************************** ATM **************************** ")
        print("\t""Welcome to your Bank Account", account['name'], end="\n\n")
        choice = 9

        while (True):
            print(" ___________________________________________________________ ")
            print("\t\t\tMAIN MENU")                                        
            print("\t\t  [1] Balance Inquiry")                              
            print("\t\t  [2] Withdrawal")                                   
            print("\t\t  [3] Deposit")                                      
            print("\t\t  [4] Change PIN")                                   
            print("\t\t  [5] Return Card")
            print("\t\t  [6] Logout and Exit")
            print(" ___________________________________________________________ ")

            choice = int(input("Choose a number in Main Menu to proceed: "))
            print("\n\n")

            if choice == 6:
                clear_console()
                confirm = input("Are you sure to logout? Y/N : ")

                if confirm in ('Y', 'y'):
                    print("Exiting...")
                    t.sleep(2)
                    print("You have been logged out. Thank you!\n\n")
                    break

                else:
                    print("Returning to main menu...")
                    t.sleep(1)
                    print("Logout Cancelled!\n\n")
                    clear_console()
                    continue
                
            elif choice in (1, 2, 3, 4, 5):
                num_of_tries = 3

                while (num_of_tries != 0):

                    if input_pin == account['pin']:
                        clear_console()
                        if choice == 1:
                            print("Loading Account Balance...")
                            t.sleep(1.5)
                            print("Your current balance is: ",
                                account['balance'], end="\n\n\n")
                            break

                        elif choice == 2:
                            clear_console()
                            # Withdrawal
                            print("Opening Cash Withdrawal...")
                            t.sleep(1.5)
                            print(" ************************************************************************************ ")
                            print(" *                                                                                  * ")
                            print(" *                                   WITHDRAWAL                                     * ")
                            print(" *                                                                                  * ")
                            print(" ************************************************************************************ ")
                            while (True):
                                     
                                withdraw_input = input(
                                    "Enter the amount you wish to withdraw or press (6) to go back to the previous menu: ")

                                if withdraw_input.lower() == '6':
                                    print("Returning to main menu...")
                                    t.sleep(1)
                                    clear_console()
                                    break

                                else:
                                    
                                    withdraw_amt = float(withdraw_input)
                                    if withdraw_amt > account['balance']:
                                        print(
                                            "You can't withdraw from that amount:", withdraw_amt)
                                        print("Please enter a lower amount. Try again!")
                                        continue

                                    else:
                                        print("Withdrawing: ", withdraw_amt)
                                        confirm = input("Confirm? Y/N : ")
                                        if confirm in ('Y', 'y'):
                                            account['balance'] -= withdraw_amt
                                            print("Amount withdrawn: ", withdraw_amt)
                                            print("Remaining balance: ",
                                            account['balance'], end="\n\n\n")
                                            accounts[account_position] = account
                                            with open("account.txt", "w") as f:
                                                for _account in accounts:
                                                    _str = str(_account['pin']) + ', ' + str(_account['balance']) + ', ' + _account['name'] + '\n'
                                                    f.write(_str)
                                            break
                                        else:
                                            print("Cancelling transaction...")
                                            t.sleep(1)
                                            print("Transaction Cancelled!\n\n")
                                            clear_console()
                                            break
                            break
                        elif choice == 3:
                            clear_console()
                            print("Loading Cash Deposit...")
                            t.sleep(1.5)
                            print(" ************************************************************************************ ")
                            print(" *                                                                                  * ")
                            print(" *                                   DEPOSIT                                        * ")
                            print(" *                                                                                  * ")
                            print(" ************************************************************************************ ")
                            deposit_input = input(
                                "Enter the amount you wish to deposit or press (6) to go back to the previous menu: ")
                            if deposit_input.lower() == '6':
                                print("Returning to main menu...")
                                t.sleep(1)
                                clear_console()
                                break
                            else:
                                deposit_amt = float(deposit_input)
                                print("Depositing: ", deposit_amt)
                                confirm = input("Confirm? Y/N : ")
                                if confirm in ('Y', 'y'):
                                    account['balance'] += deposit_amt
                                    print("Amount deposited: ", deposit_amt)
                                    print("Updated balance: ",
                                        account['balance'], end="\n\n\n")
                                    accounts[account_position] = account
                                    with open("account.txt", "w") as f:
                                        for _account in accounts:
                                            _str = str(_account['pin']) + ', ' + str(_account['balance']) + ', ' + _account['name'] + '\n'
                                            f.write(_str)
                                else:
                                    print("Cancelling transaction...")
                                    t.sleep(1)
                                    print("Transaction Cancelled!\n\n")
                                    print("Returning to main menu...")
                                    t.sleep(1)
                                    clear_console()
                            break
                        elif choice == 4:
                            clear_console()
                            print("Opening Change PIN...")
                            t.sleep(1.5)
                            print(" ************************************************************************************ ")
                            print(" *                                                                                  * ")
                            print(" *                                  CHANGE 4 PIN                                    * ")
                            print(" *                                                                                  * ")
                            print(" ************************************************************************************ ")
                            pin_input = input(
                                "Enter your new 4-digit PIN or press (6) to go back to main menu: ")
                            if pin_input == '6':
                                print("Returning to main menu...")
                                t.sleep(1)
                                clear_console()
                                break
                            else:
                                new_pin = int(pin_input)
                                confirm = input("Confirm? Y/N : ")
                                if confirm in ('Y', 'y'):
                                    account['pin'] = new_pin
                                    print("Your PIN has been changed successfully.")
                                    print("New PIN: ", account['pin'], end="\n\n\n")
                                    with open("account.txt", "w") as f:
                                        for account_ in accounts:
                                            _str = str(account_['pin']) + ', ' + str(account_['balance']) + ', ' + account_['name'] + '\n'
                                            f.write(_str)
                                else:
                                    print("Cancelling transaction...")
                                    t.sleep(1)
                                    print("Transaction Cancelled!\n\n")
                                    print("Returning to main menu...")
                                    t.sleep(1)
                                    clear_console()
                            break

                        elif choice == 5:
                            clear_console()
                            print("Returning card...")
                            t.sleep(1)
                            print(" ************************************************************************************ ")
                            print(" *                                                                                  * ")
                            print(" *                                  RETURN CARD                                     * ")
                            print(" *                                                                                  * ")
                            print(" ************************************************************************************ ")
                            print("Card returned. Thank you!")
                            break
                    else:
                        num_of_tries -= 1
                        if num_of_tries == 0:
                            print("You have exceeded the maximum number of tries.")
                            print("Exiting...")
                            t.sleep(2)
                            break
                        else:
                            print("Incorrect PIN. Please try again.")
                            input_pin = int(input("Enter your 4-digit PIN: "))
            else:
                clear_console()
                print("Invalid choice. Please try again.")
        break
    else:
        clear_console()
        t.sleep(2)
        num_of_tries -= 1
        if num_of_tries == 0:
            print("You have exceeded the maximum number of tries.")
            print("Exiting...")
            t.sleep(2)
            break
        else:
            print("Incorrect PIN. Please try again.")
            print("You have", num_of_tries, "login remaining!\n\n")