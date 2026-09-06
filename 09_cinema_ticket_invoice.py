class MovieTicket:
    def __init__(self, ticket_id : int, customer_name : str, movie_name : str, seat_type : str, seats_count : int, combo_meal : bool = False):
        self.ticket_id = ticket_id
        self.cust_name = customer_name
        self.mov_name = movie_name
        self.seat_type = seat_type
        self.seats_count = seats_count
        self.combo_meal = combo_meal

    def seat_cost(self):
        p = self.seat_type

        if p == "Silver":
            price_per_seat = 180

        elif p == "Gold":
            price_per_seat = 250

        elif p == "Recliner":
            price_per_seat = 450

        return (price_per_seat * self.seats_count)
        

    def combo_cost(self):

        if self.combo_meal == True:
            return 200 * self.seats_count

        else:
            return 0 

    def meal_status(self):

        if self.combo_meal == True:
            return "Yes"

        else:
            return "No"

    def subtotal(self):
        return (self.seat_cost() + self.combo_cost())

    def group_disc(self):
        c = self.seats_count

        if c >= 5:
            return self.subtotal() * 0.15

        elif c >= 3:
            return self.subtotal() * 0.08

        else:
            return 0

    def calc_gst(self):
        taxable_amount = (self.subtotal() - self.group_disc())

        return taxable_amount * 0.18

    def grand_total(self):
        return ((self.subtotal() - self.group_disc()) + self.calc_gst())

    def generate_ticket(self):
        return f"""
===================================================
                KHINVASARA CINEPLEX
===================================================
Customer Name        : {self.cust_name}
Ticket ID            : {self.ticket_id}
---------------------------------------------------
Movie Title          : {self.mov_name}
Seat Type            : {self.seat_type}
No. Of Seats         : {self.seats_count}
---------------------------------------------------
Snack Combo Included : {self.meal_status()}
---------------------------------------------------
                    CHARGES
---------------------------------------------------
Ticket Base Cost     : ₹{self.seat_cost():>10.2f}
Combo Add-On Cost    : ₹{self.combo_cost():>10.2f}
Subtotal             : ₹{self.subtotal():>10.2f}
Group Discount       : ₹{self.group_disc():>10.2f}
GST (18 %)           : ₹{self.calc_gst():>10.2f}

FINAL PAYABLE        : ₹{self.grand_total():>10.2f}
===================================================
                    THANK YOU!
===================================================\n\n\n
"""


customers = [
    MovieTicket(1231, "Farhan", "Bahubali", "Silver", 6, True),
    MovieTicket(1232, "Salman", "Drishyam", "Gold", 4),
    MovieTicket(1233, "Daniel", "Spiderman", "Recliner", 2, True),
    MovieTicket(1234, "Anzar", "Captain America", "Recliner", 12),
    MovieTicket(1235, "Yash", "Dabangg", "Gold", 20, True)
]


for i, customers in enumerate(customers, start = 1):
    print(f"{i}:- {customers.generate_ticket()}")
