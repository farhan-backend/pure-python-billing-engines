class EVChargingSession:

    green_cess_rate = 0.05
    gst_rate = 0.18

    def __init__(self, session_id : str, driver_name : str, charger_type : str, energy_consumed_kwh : float, charging_minutes : int, battery_cooling : bool = False, fleet_membership : bool = False):
        self.id = session_id
        self.name = driver_name
        self.charger_type = charger_type
        self.energy_consumed = energy_consumed_kwh
        self.charging_minutes = charging_minutes
        self.battery_cooling = battery_cooling
        self.membership = fleet_membership

    def base_rate_per_kwh(self):
        c = self.charger_type

        if c == "Standard AC":
            return 14

        elif c == "Fast DC":
            return 22

        elif c == "Ultra DC":
            return 32

        else:
            return 0

    def base_energy_cost(self):
        a = self.base_rate_per_kwh()
        b = self.energy_consumed

        base_cost = a * b

        return base_cost
    
    def parking_allowance(self):
        c = self.charger_type

        if c == "Standard AC":
            return 180

        elif c in ("Fast DC", "Ultra DC"):
            return 45

        else:
            return 0

    def idle_parking_fee(self):
        c = self.charger_type
        m = self.charging_minutes
        p = self.parking_allowance()

        if c in ("Fast DC", "Ultra DC") and m > p:
            return (m - p) * 8

        elif c == "Standard AC" and m > p:
            return (m - p) * 2
        
        else:
            return 0

    def thermal_management(self):
        b = self.battery_cooling

        if b:
            return 150

        else:
            return 0

    def gross_amount(self):
        a = self.base_energy_cost()
        b = self.idle_parking_fee()
        c = self.thermal_management()

        amount = a + b + c

        return amount

    def fleet_discount(self):
        f = self.membership
        e = self.energy_consumed
        g = self.gross_amount()

        if f:

            if e > 50:
                return g * 0.15
            
            else:
                return g * 0.10

        else:
            return 0
    def subtotal(self):
        a = self.gross_amount()
        b = self.fleet_discount()

        subtotal = a - b

        return subtotal

    def green_cess(self):
        s = self.subtotal()
        a = self.green_cess_rate

        green_cess = s * a

        return green_cess

    def gst(self):
        s = self.subtotal()
        a = self.gst_rate

        gst = s * a

        return gst

    def total_tax(self):
        a = self.green_cess()
        b = self.gst()

        total_tax = a + b

        return total_tax

    def total_payable(self):
        a = self.subtotal()
        b = self.total_tax()

        total_amount = a + b

        return total_amount

    def battery_cooling_status(self):
        a = self.battery_cooling

        if a:
            return "Yes! Battery Cooling Opted"

        else:
            return "Not Opted"

    def membership_status(self):
        a = self.membership

        if a:
            return "Active! (Discount Applied)"

        else:
            return "Not Available"

    def generate_charge_summary(self):
        return f"""
========================================================================
                   SMART EV FAST CHARGING STATION
========================================================================
                        DRIVER INFORMATION
------------------------------------------------------------------------
Driver Name                        : {self.name}
Session ID                         : {self.id}
------------------------------------------------------------------------
                       CHARGING INFORMATION
------------------------------------------------------------------------
Charger Type                       : {self.charger_type}
Session Duration                   : {self.charging_minutes} Minutes
Parking Time Allowed               : {self.parking_allowance()} Minutes
Energy Consumed                    : {self.energy_consumed} kWh
Battery Pre-Cooling                : {self.battery_cooling_status()}
Fleet Membership                   : {self.membership_status()}
------------------------------------------------------------------------
                        CHARGES BREAKDOWN
------------------------------------------------------------------------
Base Energy Cost                   : ₹{self.base_energy_cost():>10.2f}
Idle Overstay Penalty              : ₹{self.idle_parking_fee():>10.2f}
Battery Pre-Cooling Service Charge : ₹{self.thermal_management():>10.2f}
------------------------------------------------------------------------
GROSS TOTAL                        : ₹{self.gross_amount():>10.2f}
------------------------------------------------------------------------
Fleet Member Discount              : ₹{self.fleet_discount():>10.2f}
Green Energy Cess  (5 %)           : ₹{self.green_cess():>10.2f}
GST  (18 %)                        : ₹{self.gst():>10.2f}
Total Tax                          : ₹{self.total_tax():>10.2f}
------------------------------------------------------------------------
TOTAL PAYABLE AMOUNT               : ₹{self.total_payable():>10.2f}
========================================================================
                            THANK YOU!
========================================================================
"""



customers = [
    EVChargingSession("EV-8801", "Rahul Verma", "Fast DC", 38.5, 60, True, False),
    EVChargingSession("EV-8802", "Zomato Fleet #14", "Fast DC", 62.0, 40, False, True),
    EVChargingSession("EV-8803", "City Ride Logistics", "Standard AC", 24.0, 210, False, True)
]


for i, customers in enumerate(customers, start = 1):
    print(f"{i}:- {customers.generate_charge_summary()}")