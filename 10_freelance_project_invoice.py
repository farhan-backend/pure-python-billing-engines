class FreelanceInvoice:
    def __init__(self, invoice_no : int, client_name : str, project_domain : str, hours_worked : int, rush_delivery : bool = False):
        self.invoice_no = invoice_no
        self.client_name = client_name
        self.project_domain = project_domain
        self.hours_worked = hours_worked
        self.rush_delivery = rush_delivery

    def hourly_rate(self):
        p = self.project_domain

        if p == "Web Development":
            base_rate = 1200

        elif p == "Data Analysis":
            base_rate = 1500

        elif p == "AI / Machine Learning":
            base_rate = 2200

        else:
            base_rate = 1000

        return base_rate * self.hours_worked

    def rush_fee(self):
        r = self.rush_delivery

        if r == True:
            return self.hourly_rate() * 0.25

        else:
            return 0
        
    def rush_status(self):

        if self.rush_delivery == True:
            return "Yes"

        else:
            return "No"
        
    def subtotal(self):
        return (self.hourly_rate() + self.rush_fee())

    def volume_discount(self):
        q = self.hours_worked
        s = self.subtotal()

        if q >= 40:
            return s * 0.10

        elif q >= 20:
            return s * 0.05

        else: 
            return 0

    def calc_gst(self):
        taxable_amount = (self.subtotal() - self.volume_discount())

        return taxable_amount * 0.18

    def final_payable(self):
        return ((self.subtotal() - self.volume_discount()) + self.calc_gst())

    def generate_invoice(self):
        return f"""
======================================================
                FREELANCE INVOICE
======================================================
Client Name             : {self.client_name}
Invoice No.             : {self.invoice_no}
------------------------------------------------------
Project Domain          : {self.project_domain}
Hours Logged            : {self.hours_worked}
Rush Delivery Status    : {self.rush_status()}
------------------------------------------------------
Base Development Cost   : ₹{self.hourly_rate():>12.2f}
Rush Delivery Surcharge : ₹{self.rush_fee():>12.2f}
Subtotal                : ₹{self.subtotal():>12.2f}
Volume Discount         : ₹{self.volume_discount():>12.2f}
GST  (18 %)             : ₹{self.calc_gst():>12.2f}

TOTAL PAYABLE AMOUNT    : ₹{self.final_payable():>12.2f}
======================================================
                    THANK YOU!
======================================================\n\n\n
"""


invoices = [
    FreelanceInvoice(1234, "Farhan", "Web Development", 15),
    FreelanceInvoice(1235, "Amaan", "Data Analysis", 25, True),
    FreelanceInvoice(1236, "Yash", "AI / Machine Learning", 45)
]


for i,freelancers in enumerate(invoices, start = 1):
    print(f"{i}:- {freelancers.generate_invoice()}")