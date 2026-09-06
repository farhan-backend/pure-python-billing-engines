class FlightBooking:

    airline_name = "EMIRATES AIRWAYS"
    gst_rate = 0.18
    airport_fee = 750

    def __init__(self, booking_id : int, passenger_name : str, travel_class : str, flight_distance : float, checked_bags_weight : float, meal_preference : str, frequent_flyer_tier : str, travel_insurance : bool = False):
        self.id = booking_id
        self.name = passenger_name
        self.travel_class = travel_class
        self.distance = flight_distance
        self.bags_weight = checked_bags_weight
        self.meal_preference = meal_preference
        self.frequent_flyer_tier = frequent_flyer_tier
        self.insurance = travel_insurance

    def base_airfare(self):
        p = self.travel_class

        if p == "Economy":
            rate_per_km = 5.5

        elif p == "Premium Economy":
            rate_per_km = 8

        elif p == "Business":
            rate_per_km = 14.5

        elif p == "First Class":
            rate_per_km = 24

        else:
            rate_per_km = 5

        return self.distance * rate_per_km

    def free_baggage_allowance(self):
        p = self.travel_class

        if p == "Economy":
            return 15

        elif p == "Premium Economy":
            return 25

        elif p == "Business":
            return 35

        elif p == "First Class":
            return 50

        else:
            return 15

    def excess_baggage_fee(self):
        a = self.bags_weight
        b = self.free_baggage_allowance()

        if a > b:
            return (a - b) * 650

        else:
            return 0

    def meal_charges(self):
        m = self.meal_preference

        if m == "None":
            return 0

        elif m == "Standard Veg":
            return 450

        elif m == "Gourmet Non-Veg":
            return 850

        elif m == "Chef Special":
            return 1600

        else:
            return 0

    def insurance_fee(self):
        t = self.insurance

        if t:
            return 1200

        else:
            return 0

    def subtotal(self):
        subtotal = self.base_airfare() + self.excess_baggage_fee() + self.insurance_fee() + self.meal_charges() + self.airport_fee

        return subtotal

    def loyalty_discount(self):
        a = self.frequent_flyer_tier

        if a == "Platinum":
            discount = 0.15

        elif a == "Gold":
            discount = 0.1

        elif a == "Silver":
            discount = 0.05

        else:
            discount = 0

        return self.base_airfare() * discount

    def gst(self):
        taxable_amount = self.subtotal() - self.loyalty_discount()

        return taxable_amount * self.gst_rate

    def final_payable(self):
        total_amount = (self.subtotal() - self.loyalty_discount()) + self.gst()

        return total_amount

    def insurance_status(self):
        i = self.insurance

        if i:
            return "Active (₹ 1200)"

        else:
            return "Not Opted"

    def meal_status(self):
        m = self.meal_preference
   
        if m == "None":
            return "No Meal selected"
    
        elif m in ("Standard Veg", "Gourmet Non-Veg", "Chef Special"):
            return f"Yes! {m} Meal is Selected"

        else:
            return "No Meal"
 
    def generate_boarding_pass_invoice(self):
        return f"""
======================================================================
                        {self.airline_name}
======================================================================
Passenger Name                 : {self.name}
Booking ID                     : {self.id}
----------------------------------------------------------------------
                        Flight Information
----------------------------------------------------------------------
Travel Class                   : {self.travel_class}
Flight Distance (In KM)        : {self.distance} KM
Route Distance                 : {self.distance} KM
----------------------------------------------------------------------
                            Luggage
----------------------------------------------------------------------
Checked Bags Weight            : {self.bags_weight} KG
Allowed Free Limit             : {self.free_baggage_allowance()} KG
----------------------------------------------------------------------
                        Ticket Information
----------------------------------------------------------------------
Meal Selected                  : {self.meal_status()}
Insurance Status               : {self.insurance_status()}
----------------------------------------------------------------------
                        CHARGES BREAKDOWN
----------------------------------------------------------------------
Base Airfare                   : ₹{self.base_airfare():>12.2f}
Excess Baggage Charges         : ₹{self.excess_baggage_fee():>12.2f}
In - Flight Meal Cost          : ₹{self.meal_charges():>12.2f}
Airport Development FEE        : ₹{self.airport_fee:>12.2f}
Travel Insurance FEE           : ₹{self.insurance_fee():>12.2f}
SUBTOTAL                       : ₹{self.subtotal():>12.2f}
Loyalty Tier Discount Applied  : ₹{self.loyalty_discount():>12.2f}
GST  (18 %)                    : ₹{self.gst():>12.2f}

FINAL TICKET PAYABLE           : ₹{self.final_payable():>12.2f}
======================================================================
                            THANK YOU!
======================================================================\n\n\n
"""


passengers = [
    FlightBooking(7001, "Farhan", "First Class", 1850, 54, "Chef Special", "Platinum", True),
    FlightBooking(7002, "Amaan", "Business", 1200, 42, "Gourmet Non-Veg", "Gold"),
    FlightBooking(7003, "Yash", "Premium Economy", 850, 24, "Standard Veg", "Silver", True),
    FlightBooking(7004, "Rahul", "Economy", 600, 22.5, "None", "None"),
    FlightBooking(7005, "Salman", "First Class", 1550, 64, "Standard Veg", "Gold", True),
    FlightBooking(7006, "Anzar", "Economy", 1880, 34, "Chef Special", "Platinum"),
    FlightBooking(7007, "Shoaib", "Standard", 1650, 50, "Gourmet Non-Veg", "Silver", True),
    FlightBooking(7008, "Kaif", "Economy", 1850, 14, "None", "None")
]


for i, passengers in enumerate(passengers, start = 1):
    print(f"{i}:- {passengers.generate_boarding_pass_invoice()}")      