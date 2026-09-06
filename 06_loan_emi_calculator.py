class LoanAccount:
    def __init__(self, loan_id : int, borrower_name : str, loan_type : str, principal : float, tenure_years : int, auto_debit : bool = False):
        self.id = loan_id
        self.borrower_name = borrower_name
        self.loan_type = loan_type
        self.principal = principal
        self.tenure_years = tenure_years
        self.auto_debit = auto_debit

    def annual_interest_rate(self):
        p = self.loan_type

        if p == "Home Loan":
            return 0.085

        elif p == "Car Loan":
            return 0.095

        elif p == "Personal Loan":
            return 0.12

        else:
            return 0.1

    def processing_fee(self):
        p = self.loan_type
        q = self.principal

        if p == "Home Loan":
            return 5000

        elif p == "Car Loan":
            return q * 0.01

        elif p == "Personal Loan":
            return q * 0.02

        else:
            return 1000

    def total_interest(self):
         total_interest = (self.principal * self.annual_interest_rate() * self.tenure_years)
         return total_interest

    def auto_debit_disc(self):

        if self.auto_debit == True:
            return self.total_interest() * 0.025

        else:
            return 0

    def total_loan_ammount(self):
        return self.principal + self.total_interest() + self.processing_fee() - self.auto_debit_disc()

    def monthly_emi(self):
        total_months = self.tenure_years * 12

        return self.total_loan_ammount() / total_months

    def auto_debit_status(self):

        if self.auto_debit == True:
            return "Active (0.25 % Rebate)"

        else:
            return "Inactive"

    def generate_loan_summary(self):

        return f"""
========================================================
                        SBI BANK
========================================================
Borrower Name                   : {self.borrower_name}
Loan ID                         : {self.id}
--------------------------------------------------------
Loan Type                       : {self.loan_type}
Tenure Years                    : {self.tenure_years}
Auto Debit Status               : {self.auto_debit_status()}
--------------------------------------------------------
Sanctioned Principal Amount     : ₹{self.principal:>12.2f}
Applicable Annual Interest Rate :  {self.annual_interest_rate() * 100:>12.2f} %
Total Interest Over Tenure      : ₹{self.total_interest():>12.2f}
Processing Fee                  : ₹{self.processing_fee():>12.2f}
--------------------------------------------------------
Total Repayment Amount          : ₹{self.total_loan_ammount():>12.2f}
Monthly EMI Payable             : ₹{self.monthly_emi():>12.2f}
========================================================
                        THANK YOU!
========================================================
"""

            
accounts = [
    LoanAccount(501, "Farhan", "Home Loan", 2500000, 15, True),
    LoanAccount(502, "Aman", "Car Loan", 850000, 5, False),
    LoanAccount(503, "Yash", "Personal Loan", 300000, 3, True)
]

for i, accounts in enumerate(accounts, start = 1):
    print(f"{i}:- {accounts.generate_loan_summary()}")