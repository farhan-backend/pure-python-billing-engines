class GymMembership:
    def __init__(self, member_id : int, member_name : str, plan_type : str, months : int, pers_trainer : bool = False):
        self.member_id = member_id
        self.member_name = member_name
        self.plan_type = plan_type
        self.months = months
        self.pers_trainer = pers_trainer

    def base_plan_cost(self):
        p = self.plan_type

        if p == "Basic":
            monthly_rate = 1200

        elif p == "Standard":
            monthly_rate = 2000

        elif p == "Premium":
            monthly_rate = 3200

        else:
            monthly_rate = 0

        return monthly_rate * self.months

    def trainer_cost(self):

        if self.pers_trainer == True:
            return (1500 * self.months)

        else: 
            return 0

    def trainer_status(self):

        if self.pers_trainer == True:
            return "Yes"

        else:
            return "No"

    def subtotal(self):
        return (self.base_plan_cost() + self.trainer_cost())

    def duration_discount(self):

        if self.months >= 12:
            return self.subtotal() * 0.20

        elif self.months >= 6:
            return self.subtotal() * 0.10

        else:
            return 0

    def calc_gst(self):
        return ((self.subtotal() - self.duration_discount()) * 0.18)

    def final_payable(self):
        return ((self.subtotal() - self.duration_discount()) + self.calc_gst())

    def gen_bill(self):
        return f"""
=============================================
                LION HEART GYM
=============================================
Member Name          : {self.member_name}
Member ID            : {self.member_id}
---------------------------------------------
Plan Type            : {self.plan_type}
Duration             : {self.months} Months
Personal Trainer     : {self.trainer_status()}
---------------------------------------------
                CHARGES
---------------------------------------------
Base Plan Cost       : ₹{self.base_plan_cost():>10.2f}
Trainer Add-on Cost  : ₹{self.trainer_cost():>10.2f}
Subtotal             : ₹{self.subtotal():>10.2f}
Discount Applied     : ₹{self.duration_discount():>10.2f}
GST (18 %)           : ₹{self.calc_gst():>10.2f}

FINAL PAYABLE AMOUNT : ₹{self.final_payable():>10.2f}
=============================================
                THANK YOU!
=============================================\n\n
"""


    

members = [
    GymMembership(1234, "Farhan", "Basic", 12, True),
    GymMembership(1235, "Anzar", "Standard", 6),
    GymMembership(1236, "Yash", "Premium", 4, True),
    GymMembership(1237, "Zaid", "Premium", 3),
    GymMembership(1238, "Ayush", "Premium", 18, True),
    GymMembership(1239, "Aslam", "Basic", 7, True),
    GymMembership(1240, "Umar", "Standard", 4)
]

for i, members in enumerate(members, start = 1):
    print(f"{i}:- {members.gen_bill()}")