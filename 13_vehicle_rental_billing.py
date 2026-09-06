class VehicleRental:
    def __init__(self, booking_id : int, customer_name : str, car_model : str, days : int, km_driven : float, late_hours : int = 0):
        self.booking_id = booking_id
        self.cust_name = customer_name
        self.car_model = car_model
        self.days = days
        self.driven = km_driven
        self.late = late_hours

    def base_rent(self):
        return (self.days * 1800)

    def extra_km_charge(self):
        p = self.driven
        allowed_km = self.days * 150
        
        if p > allowed_km:
            return (p - allowed_km) * 12

        else: 
            return 0

    def late_fee(self):
        return (self.late * 150)

    def calc_gst(self):
        return ((self.base_rent() + self.extra_km_charge() + self.late_fee()) * 0.18)

    def total_invoice_amount(self):
        return (self.base_rent() + self.extra_km_charge() + self.late_fee() + self.calc_gst())

    def generate_invoice(self):
        return f"""
============================================================
                    VEHICLE RENTAL
============================================================
Customer Name                            : {self.cust_name}
Booking ID                               : {self.booking_id}
------------------------------------------------------------
Car Model                                : {self.car_model} 
Days Rented                              : {self.days} Days
------------------------------------------------------------
Distance Driven (In KM)                  : {self.driven} KM
------------------------------------------------------------
                        CHARGES
------------------------------------------------------------
Base Rent (₹1800 / Day)                  : ₹{self.base_rent():>10.2f}
Extra Distance Charge (₹12 / Extra KM)   : ₹{self.extra_km_charge():>10.2f}
Late Return Fee (₹150 / Late Hour)       : ₹{self.late_fee():>10.2f}
GST (18 %)                               : ₹{self.calc_gst():>10.2f}

TOTAL PAYABLE AMOUNT                     : ₹{self.total_invoice_amount():>10.2f}
============================================================
"""



customers = [
    VehicleRental(1234, "Farhan", "Fortuner", 3, 170, 4),
    VehicleRental(1235, "Zaid", "Innova", 6, 140),
    VehicleRental(1245, "Khan", "Indica", 9, 290)
    
]

for customers in customers:
    print(customers.generate_invoice())