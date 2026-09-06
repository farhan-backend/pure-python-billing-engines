class Employee:
    def __init__(self, emp_id : int, name : str, monthly_salary : float, rating : int):
        self.id = emp_id
        self.name = name
        self.salary = monthly_salary
        self.rating = rating

    def annual_salary(self):
        return self.salary * 12

    def calc_bonus(self):
        p = self.rating
        if p == 5:
            return self.annual_salary() * 0.20

        elif p == 4:
            return self.annual_salary() * 0.10

        elif p == 3:
            return self.annual_salary() * 0.05

        else:
            return 0

    def calc_tax(self):
        total_earning = self.annual_salary() + self.calc_bonus()

        if total_earning > 500000:
            return total_earning * 0.10

        else:
            return 0

    def net_pay(self):
        return (self.annual_salary() + self.calc_bonus()) - self.calc_tax()

    def payslip(self):
        return f"""
==================================================
                 ANNUAL PAYSLIP                  
==================================================
Emp ID: {self.id:<8} | Name: {self.name}
Performance Rating: {self.rating} / 5
--------------------------------------------------
Base Annual Salary : ₹{self.annual_salary():>12.2f}
Bonus Earned       : ₹{self.calc_bonus():>12.2f}
Tax Deducted       : ₹{self.calc_tax():>12.2f}
--------------------------------------------------
Net In-Hand Pay    : ₹{self.net_pay():>12.2f}
==================================================
"""




data = [
    Employee(12345671, "Farhan", 50000, 5),
    Employee(12345672, "Anzar", 60000, 4),
    Employee(12345673, "Yash", 30000, 4)
]

for employee in data:
    print(employee.payslip())