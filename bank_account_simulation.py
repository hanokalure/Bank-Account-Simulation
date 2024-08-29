user={}
initial_balance=0

def create_ac():
    print("==================== CREATE ACCOUNT =====================")
    name=str(input("Enter the name of the account holder : "))

    while True:
        try:
            pin=int(input("Create a 4-digit pin : "))
            if len(str(pin)) !=4:
                print("Pin must be only of 4 digit.")
                continue
            break
        except ValueError:
            print("The pin must contain only numeric values.")

    while True:
        try:
            account_number=int(input("Create a 6 digit account number : "))
            if len(str(account_number)) !=6:
                print("Account number must be 6 digit.")
                continue
            break
        except ValueError:
            print("The Account number must contain only numeric values.")

     
    balance=float(input("Enter the intial balance amount : "))
    while balance<1000:
        print("The minimum amount to deposit is Rs.1000")
        balance=float(input("Enter the intial balance amount : "))

    user[name]={"Pin":pin,"Account Number":account_number,"Balance":balance}
    print("Account created sucessfully.")
    print("==================== ACCOUNT DETAILS =====================")
    print(user)
    print("==========================================================")
    main()
    
    
def deposit():
    print("====================== DEPOSIT ===========================")
    if user:
        account_number=int(input("Account number : "))
        pin=int(input("Pin : "))
        for name,data in user.items():
            stored_account_number=data["Account Number"]
            stored_pin=data["Pin"]
            if stored_account_number==account_number and stored_pin==pin:
                amount=float(input("Amount : "))
                data["Balance"] += amount
                print("Amount deposited successfully.")
                print(f"New balance: {data['Balance']}")
            else:
                print("Incorrect Credentials")
    
    else:
        print("No user exists")
    print("=============================================================")
    main()

def withdraw():
    print("======================= WITHDRAW ===========================")
    if user:
        account_number=int(input("Account number : "))
        pin=int(input("Pin : "))
        for name,data in user.items():
            stored_pin=data["Pin"]
            stored_account_number=data["Account Number"]
            if stored_account_number==account_number and stored_pin==pin:
                withdraw_amount=float(input("Amount : "))
                current_ac_balance=data["Balance"]
                if withdraw_amount<current_ac_balance-1000:
                    data["Balance"] -= withdraw_amount
                    print("Amount withdraw sucessfully")
                    print(f"Balance : {data["Balance"]}")
                else:
                    print("The minimum account balance to maintain is Rs.1000")
            
            else:
                print("Incorrect Credentials")
    else:
        print("No user exists")
    print("=================================================================")
    main()


def check_balance():
    print("======================== ACCOUNT BALANCE ==========================")
    if user:
        account_number=int(input("Account Number : "))
        pin=int(input("Pin : "))
        for name,data in user.items():
            stored_ac_number=data["Account Number"]
            stored_pin=data["Pin"]
            if stored_ac_number==account_number and stored_pin==pin:
                print(f"Balance : {data["Balance"]}")
            else:
                print("Incorrect Creentials")
    else:
        print("No user exists")
    print("======================================================================")
    main()

def main():
    print("================ Bank Account Simulation ================")
    print("1->CREATE ACCOUNT")
    print("2->DEPOSIT")
    print("3->WITHDRAW")
    print("4->CHECK BALANCE")
    print("5->Exit")
    option=int(input("Enter any on of them : "))
    print("=========================================================")


    if (option==1):
        create_ac()
    elif (option==2):
        deposit()
    elif (option==3):
        withdraw()
    elif(option==4):
        check_balance()
    elif(option==5):
        print("Exiting Good Bye!")
    else:
        print("Invalid Input")

main()
