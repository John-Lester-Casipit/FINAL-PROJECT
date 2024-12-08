accounts = {}

def Create_Account():
    Account_Name = input("Enter account name: ")
    if Account_Name in accounts:
        print("Account already exists!")
    else:
        accounts[Account_Name] = 0
        print(f"Account created successfully for {Account_Name}.")


def denomination(amount):
    print("\nDenomination Breakdown:")
    answer1 = amount // 1000
    ans1 = amount % 1000
    answer2 = ans1 // 500
    ans2 = ans1 % 500
    answer3 = ans2 // 200
    ans3 = ans2 % 200
    answer4 = ans3 // 100
    ans4 = ans3 % 100
    answer5 = ans4 // 50
    ans5 = ans4 % 50
    answer6 = ans5 // 20
    ans6 = ans5 % 20
    answer7 = ans6 // 10
    ans7 = ans6 % 10
    answer8 = ans7 // 5
    ans8 = ans7 % 5
    answer9 = ans8 // 1
    ans9 = ans8 % 1


    print(answer1,"-1000")
    
    print(answer2,"-500")

    print(answer3,"-200")

    print(answer4,"-100")

    print(answer5,"-50")

    print(answer6,"-20")

    print(answer7,"-10")

    print(answer8,"-5")

    print(answer9,"-1")


def Deposit():
    Account_Name = input("Enter your account name: ")
    if Account_Name in accounts:
        try:
            amount = int(input("Enter amount to deposit : "))
            if amount > 0:
                accounts[Account_Name] += amount
                print(f"Deposited {amount} successfully. New balance: {accounts[Account_Name]}")
                denomination(amount)
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")



def Check_Balance():
    username = input("Enter your username: ")
    if username in accounts:
        print(f"Your balance: {accounts[username]}")
    else:
        print("ACCOUNT NOT FOUND!")



def Withdraw():
    username = input("Enter your username: ")
    if username in accounts:
        try:
            amount = int(input("Enter amount to withdraw (whole numbers only): "))
            if 0 < amount <= accounts[username]:
                accounts[username] -= amount
                print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                denomination(amount)
            else:
                print("Insufficient Amount!")
        except ValueError:
            print("Invalid input! Please enter a exact amount.")
    else:
        print("ACCOUNT NOT FOUND!")


def options():
    while True:
        print("\n\tWELCOME TO\nTELLYBOOOGHHSS BANKING SYSTEM")
        print("A. Create a New Account")
        print("B. Deposit")
        print("C. Withdraw Money")
        print("D. Check Balance")
        print("E. Exit")
        choice = input("Choose an option (A - E): ")

        if choice == 'A':
            Create_Account()
        elif choice == 'B':
            Deposit()
        elif choice == 'C':
            Withdraw()
        elif choice == 'D':
            Check_Balance()
        elif choice == 'E' or "Exit":
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid option. Please try again.")

options()