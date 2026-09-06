class HospitalBilling:
    def __init__(self, patient_id : int, patient_name : str, room_type : str, days_admitted : int, surgery_cost : float = 0, has_insurance : bool = False):
        self.id = patient_id
        self.name = patient_name
        self.room = room_type
        self.days = days_admitted
        self.surgery_cost = surgery_cost
        self.has_insurance = has_insurance

    def room_charges(self):
        p = self.room

        if p == "General":
            daily_rate = 1500

        elif p == "Semi-Private":
            daily_rate = 3000

        elif p == "ICU":
            daily_rate = 7000

        else:
            daily_rate = 2000

        return (daily_rate * self.days)

    def doctor_visit_fee(self):
        return self.days * 800

    def subtotal(self):
        subtotal = self.room_charges() + self.doctor_visit_fee() + self.surgery_cost

        return subtotal

    def insurance_coverage(self):
        i = self.has_insurance

        if i == True:
            return self.subtotal() * 0.70

        else:
            return 0

    def hospital_tax(self):
        taxable_amount = self.subtotal() - self.insurance_coverage()

        return taxable_amount * 0.05

    def final_payable(self):
        total_amount = ((self.subtotal() - self.insurance_coverage()) + self.hospital_tax())

        return total_amount

    def insurance_status(self):
        i = self.has_insurance

        if i == True:
            return "Covered (70 %)"

        else:
            return "Nothing"

    def generate_bill(self):
        return f"""
=======================================================
                    CITY HOSPITAL
=======================================================
Patient Name                  : {self.name}
Patient ID                    : {self.id}
-------------------------------------------------------
Room Type                     : {self.room}
Days Admited                  : {self.days}
Insurance Status              : {self.insurance_status()}
-------------------------------------------------------
Room Charges                  : ₹{self.room_charges():>12.2f}
Doctor Consultation FEE       : ₹{self.doctor_visit_fee():>12.2f}
Surgery Cost                  : ₹{self.surgery_cost:>12.2f}
Subtotal                      : ₹{self.subtotal():>12.2f}
Insurance Claim Deduction     : ₹{self.insurance_coverage():>12.2f}
Service TAX  (5 %)            : ₹{self.hospital_tax():>12.2f}

FINAL PAYABLE AMOUNT          : ₹{self.final_payable():>12.2f}
=======================================================
                      THANK YOU!
=======================================================\n\n\n
"""



patients = [
    HospitalBilling(901, "Farhan", "General", 4, 0, False),
    HospitalBilling(902, "Amaan", "ICU", 6, 45000, True),
    HospitalBilling(903, "Yash", "Semi-Private", 10, 15000, True),
    HospitalBilling(904, "Siddhu", "General", 15, 100000, True),
    HospitalBilling(905, "Salman", "ICU", 12, 50000, False)
]


for i, patients in enumerate(patients, start = 1):
    print(f"{i}:- {patients.generate_bill()}")