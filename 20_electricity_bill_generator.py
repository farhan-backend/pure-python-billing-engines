class Electricity:
    def __init__(self, customer_no : int, name : str, units_consumed : float):
        self.customer_no = customer_no
        self.name = name
        self.consumed = units_consumed

    def energy_charge(self):
        p = self.consumed

        if p <= 100:
            return (p * 4.5)

        elif p <= 200:
            return ((p - 100) * 7.5) + (100 * 4.5)

        else:
            return ((p - 200) * 12.4) + (100 * 7.5) + (100 * 4.5)
        
    def fixed_charge(self):
        return 125

    def calc_tax(self):
        return ((self.energy_charge() + self.fixed_charge()) * 0.16)

    def total_bill(self):
        return (self.energy_charge() + self.fixed_charge() + self.calc_tax())

    def create_bill(self):
        return f'''
{'=' * 70}
{'ELECTRICITY BILL':^70}
{'=' * 70}
Name                             : {self.name}
Consumer No.                     : {self.customer_no}
Total units consumed             : {self.consumed}
{'-' * 70}
{'CHARGES':^70}
{'-' * 70}
Energy Charges                   : ₹{self.energy_charge():>10.2f}
Fixed Meter Charge               : ₹{self.fixed_charge():>10.2f}
Energy Duty (16 %)               : ₹{self.calc_tax():>10.2f}

TOTAL PAYABLE AMOUNT             : ₹{self.total_bill():>10.2f}
{'-' * 70}
{'THANK YOU!':^70}
{'=' * 70}
{'\n' * 5}
'''

consumers = [
    Electricity(1, "Rehan", 500),
    Electricity(2, "Rahul", 295),
    Electricity(3, "Raj", 280.9)
]

for i, consumers in enumerate(consumers, start = 1):
    print(f"{i}:- {consumers.create_bill()}")
