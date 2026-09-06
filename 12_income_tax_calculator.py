class BudgetCalculator:

    def __init__(self, salary, expenses):
        self.salary = salary
        self.expenses = expenses
        self.savings = salary - expenses
        self.yearly_income = salary * 12
        self.yearly_expense = expenses * 12
        self.annual_savings = self.yearly_income - self.yearly_expense

    def calculate_tax(self):
        if self.yearly_income < 600000:
            return 0.0
        
        elif self.yearly_income >= 5000000:
            return self.yearly_income * 0.33
        
        elif self.yearly_income >= 1800000:
            return self.yearly_income * 0.20
        
        elif self.yearly_income >= 600000:
            return self.yearly_income * 0.10

    def display_report(self):
        print("\n-------------------------Income Tax-------------------------\n")

        tax = self.calculate_tax()

        if tax == 0:
            print("No Income TAX Needed")

        else:
            print(f"You will have to Pay ₹{tax:.2f} as Income TAX Every Year")


        print("\n-----------------Financial Record Per Month-----------------\n")

        if self.expenses > self.salary:
            print("You are Spending more than you Earn.")

        elif self.savings == 0:
            print("You cleared your Budget Perfectly, but try to Save Some Money next Month.")

        else:
            print(f"Great job! You saved ₹{self.savings} This Month")
            

        print("\n-----------------Financial Record Per Year-----------------\n")

        print(f"Your Annual Earnings are ₹{self.yearly_income}")
        print(f"Your Annual Expenses are ₹{self.yearly_expense}")

        after_tax_savings = self.annual_savings - tax

        if tax == 0:
            print(f"You will save ₹{self.annual_savings} Every Year")

        else:
            print(f"You will save ₹{after_tax_savings:.2f} After Paying Income Tax Every Year")



while True:
    print("\n-------------------------Budget Calculator-------------------------")

    salary = int(input("Enter your Total Monthly Income in (₹): "))
    expenses = int(input("Enter your Total Monthly Expense in (₹): "))

    calc = BudgetCalculator(salary, expenses)
    calc.display_report()

    print("\n-------------------------THANK YOU-------------------------\n")
    print("This Budget Calculator is made by: Mohammed Farhan")
    print("\nNote: This Budget Calculator is based on the Income Tax Slabs of India")
    print("\nThe End!\n")

    cont = input("Do you want to calculate another budget? Enter ('y') for YES or ('n') for NO: ").lower()

    if cont == 'n':
        break

