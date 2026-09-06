class ProductOrder:

    def __init__(self, order_id : int, customer_name : str, item_name : str, unit_price : float, quantity : float):
        self.order_id = order_id
        self.customer_name = customer_name
        self.item_name = item_name
        self.unit_price = unit_price
        self.quantity = quantity

    def subtotal(self):
        return self.unit_price * self.quantity

    def discount(self):
        q = self.quantity
        if q >= 5:
            return self.subtotal() * 0.15

        elif q >= 3:
            return self.subtotal() * 0.10

        else:
            return 0 

    def discounted_price(self):
        return self.subtotal() - self.discount()

    def calc_gst(self):
        return self.discounted_price() * 0.18

    def grand_total(self):
        return self.discounted_price() + self.calc_gst()

    def invoice(self):
        return f"""
==================================================
                 INVOICE                 
==================================================
Customer Name      : {self.customer_name}
Order ID           : {self.order_id}
--------------------------------------------------
Item Name          : {self.item_name}
Unit Price         : ₹{self.unit_price}
Quantity           : {self.quantity}
--------------------------------------------------
Subtotal           : ₹{self.subtotal():>10.2f}
Discount Applied   : ₹{self.discount():>10.2f}
GST (18 %)         : ₹{self.calc_gst():>10.2f}
--------------------------------------------------
Final Amount       : ₹{self.grand_total():>10.2f}
==================================================\n\n\n
"""


order = [
    ProductOrder(12345678, "Farhan", "Sugar", 60, 3.5),
    ProductOrder(12345679, "Rahul", "Cashew", 900, 5),
    ProductOrder(12345680, "Yash", "Video Game", 400, 2),
]

i = 1

for i, order in enumerate(order, start = 1):
    print(f"{i}:- {order.invoice()}")
