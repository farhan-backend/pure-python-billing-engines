class CloudBilling:
    def __init__(self, account_id : int, company_name : str, tier : str, hours_active : float, bandwidth_gb : float, reserved_instance : bool = False):
        self.id = account_id
        self.company = company_name
        self.tier = tier
        self.hours_active = hours_active
        self.bandwidth = bandwidth_gb
        self.reserved_instance = reserved_instance

    def compute_charges(self):
        t = self.tier

        if t == "Micro":
            hourly_rate = 3.5

        elif t == "Standard":
            hourly_rate = 12

        elif t == "Enterprise":
            hourly_rate = 35

        else:
            hourly_rate = 8

        return self.hours_active * hourly_rate

    def bandwidth_cost(self):
        b = self.bandwidth

        if b <= 100:
            return 0

        else:
            return (self.bandwidth - 100) * 1.5

    def subtotal(self):
        subtotal = self.compute_charges() + self.bandwidth_cost()

        return subtotal

    def reserved_discount(self):
        i = self.reserved_instance

        if i == True:
            return self.subtotal() * 0.2

        else:
            return 0

    def cloud_tax(self):
        taxable_amount = self.subtotal() - self.reserved_discount()

        return taxable_amount * 0.18

    def final_payable(self):
        total_amount = (self.subtotal() - self.reserved_discount()) + self.cloud_tax()

        return total_amount

    def plan_type_status(self):
        i = self.reserved_instance

        if i == True:
            return "Reserved (20 % OFF)"

        else:
            return "On-Demand"

    def generate_invoice(self):
        return f"""
================================================
            GOOGLE CLOUD SERVER
================================================
Company Name                 : {self.company}
Account ID                   : {self.id}
------------------------------------------------
Server Tier                  : {self.tier}
Active Hours Logged          : {self.hours_active} Hours
Bandwidth Consumed           : {self.bandwidth} GB
Instance Contract Status     : {self.bandwidth}
------------------------------------------------
Base Compute Cost            : ₹{self.compute_charges():>10.2f}
Bandwidth Overage Cost       : ₹{self.bandwidth_cost():>10.2f}
Subtotal                     : ₹{self.subtotal():>10.2f}
Reserved Contract Discount   : ₹{self.reserved_discount():>10.2f}
GST (18 %)                   : ₹{self.cloud_tax():>10.2f}

TOTAL PAYABLE AMOUNT         : ₹{self.final_payable():>10.2f}
================================================
                THANK YOU!
================================================\n\n\n
"""


clients = [
    CloudBilling(4001, "ByteWave Tech", "Standard", 720, 85, False),
    CloudBilling(4002, "Nexus Gaming", "Enterprise", 720, 1450.5, True),
    CloudBilling(4003, "Alpha Labs", "Micro", 250, 210, False),
    CloudBilling(4004, "Amazon", "Enterprise", 475, 5000, True),
    CloudBilling(4005, "Techno Gamers", "Standard", 500, 2200, False),
]

for i, clients in enumerate(clients, start = 1):
    print(f"{i}:- {clients.generate_invoice()}") 
