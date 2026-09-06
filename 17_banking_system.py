class Account:
     
    def __init__(self, bal):
        self.bal = bal

    def debit(self, amount):
        if amount > self.bal:
            print("Processing.....\n")
            print("Insufficient Balance!\n")

        else:
            self.bal -= amount
            print(f"₹{amount} debited from your Bank Account.")
            print(f"Remaining Balance is ₹{self.current_bal():.2f} in your Bank Account.")


    def credit(self, amount):
        self.bal += amount
        print("Processing.....\n")
        print(f"₹{amount} added to your Bank Account.")
        print(f"Current Balance is ₹{self.current_bal():.2f} in your Bank Account.")
        

    def current_bal(self):
        return self.bal
    
initial_balance = float(input("Enter your current Bank balance (in ₹): "))
acc = Account(initial_balance)

while True:
    print()
    print("What do you want to do?")
    act = input("Type (('c') for Credit or ('d') for Debit or ('e') for Exit): ")
    print()

    if act == "c":
        credit = float(input("Enter how much money you want to Credit to your Bank Account: "))
        print()

        acc.credit(credit)


    elif act == "d":
        debit = float(input("Enter how much money you want to Debit from your Bank Account: "))
        print()

        acc.debit(debit)

    elif act == "e":
        print("----------THANK YOU!----------")
        break

    else:
        print("Invalid Choice, please enter 'c', 'd', 'e'.")

    print("-----------THANK YOU!-----------\n\n")