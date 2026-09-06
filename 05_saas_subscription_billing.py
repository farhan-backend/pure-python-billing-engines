class SaasCloud:

    gst_rate = 0.18

    def __init__(self, client_id : int, company_name : str, tier : str, active_users : int, storage_gb : float, custom_domain : bool = False, annual_billing : bool = False):
        self.id = client_id
        self.company_name = company_name
        self.tier = tier
        self.active_users = active_users
        self.storage = storage_gb
        self.custom_domain = custom_domain
        self.annual_billing = annual_billing

    def base_tier_cost(self):
        t = self.tier

        if t == "Starter":
            return 1500

        elif t == "Professional":
            return 5000

        elif t == "Enterprise":
            return 13000

        else:
            return 0

    def users_allowed(self):
        t = self.tier

        if t == "Starter":
            return 5

        elif t == "Professional":
            return 25

        elif t == "Enterprise":
            return 100

        else:
            return 0

    def extra_user_cost(self):
        t = self.tier
        u = self.active_users
        v = self.users_allowed()

        if t == "Starter" and u > v:
            return (u - v) * 200

        elif t == "Professional" and u > v:
            return (u - v) * 150

        elif t == "Enterprise" and u > v:
            return (u - v) * 100

        else:
            return 0

    def free_data(self):
        t = self.tier

        if t == "Starter":
            return 20

        elif t == "Professional":
            return 100

        elif t == "Enterprise":
            return 500

        else:
            return 0
      
    def extra_storage_cost(self):
        t = self.tier
        s = self.storage
        u = self.free_data()

        if t == "Starter" and s > u:
            return (s - u) * 15

        elif t == "Professional" and s > u:
            return (s - u) * 10

        elif t == "Enterprise" and s > u:
            return (s - u) * 6

        else:
            return 0

    def add_on_cost(self):
        d = self.custom_domain

        if d:
            return 799

        else:
            return 0

    def gross_total(self):
        a = self.base_tier_cost()
        b = self.extra_user_cost()
        c = self.extra_storage_cost()
        d = self.add_on_cost()

        gross_total = (a + b + c + d)

        return gross_total

    def annual_discount(self):
        a = self.annual_billing
        b = self.gross_total()

        if a:
            return b * 0.20

        else:
            return 0

    def subtotal(self):
        a = self.gross_total()
        b = self.annual_discount()

        subtotal = a - b

        return subtotal

    def tax(self):
        a = self.subtotal()
        b = self.gst_rate

        tax = a * b

        return tax

    def total_payable(self): 
        a = self.subtotal()
        b = self.tax()

        total_amount = a + b

        return total_amount

    def annual_billing_status(self):
        a = self.annual_billing

        if a:
            return "Yearly Billing (20 % Billing Discount Applied)"

        else:
            return "Monthly Billing"

    def generate_invoice(self):
        return f"""
====================================================================================
                              SAAS BILLING SYSTEM
====================================================================================
                                User Information
------------------------------------------------------------------------------------
Company Name                     : {self.company_name}
Client ID                        : {self.id}
------------------------------------------------------------------------------------
                                Plan Information
------------------------------------------------------------------------------------
Plan Tier                        : {self.tier}
Billing Cycle                    : {self.annual_billing_status()}
Users Count                      : {self.active_users}
Users Allowed                    : {self.users_allowed()}
Storage Logged                   : {self.storage} GB
Storage Free                     : {self.free_data()} GB
------------------------------------------------------------------------------------
                                Charges Breakdown
------------------------------------------------------------------------------------
Base Tier Cost                   : ₹{self.base_tier_cost():>12.2f}
Extra User Charges               : ₹{self.extra_user_cost():>12.2f}
Extra Storage Cost               : ₹{self.extra_storage_cost():>12.2f}
Add-On Charges                   : ₹{self.add_on_cost():>12.2f}
------------------------------------------------------------------------------------
GROSS AMOUNT                     : ₹{self.gross_total():>12.2f}
------------------------------------------------------------------------------------
Annual Billing Discount          : ₹{self.annual_discount():>12.2f}
GST   (18 %)                     : ₹{self.tax():>12.2f}
------------------------------------------------------------------------------------
FINAL PAYABLE AMOUNT             : ₹{self.total_payable():>12.2f}
====================================================================================
                                    THANK YOU!
====================================================================================\n\n\n\n
"""



companies = [
    SaasCloud(1001, "Apex Dynamics", "Starter", 8, 35, True, False),
    SaasCloud(1002, "Nexa Tech Solutions", "Professional", 40, 250, True, True),
    SaasCloud(1003, "Global Streamline", "Enterprise", 90, 450, False, True)
]



for i, companies in enumerate(companies, start = 1):
    print(f"{i}:- {companies.generate_invoice()}")