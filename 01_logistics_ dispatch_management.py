class ShipmentOrder:
    base_cgst_rate = 0.09
    base_sgst_rate = 0.09
    base_igst_rate = 0.18
    fuel_surcharge_rate = 0.18
    carbon_offset_fee_per_km = 0.25

    def __init__(self, tracking_id : str, client_name : str, origin_hub : str, destination_city : str, transport_mode : str, cargo_category : str, weight_kg : float, volume_cbm : float, distance_km : float, is_interstate : bool = False, priority_handling : bool = False, insurance_opted : bool = False, declared_value : float = 0, enterprise_account : bool = False):
        self.tracking_id = tracking_id
        self.name = client_name
        self.hub = origin_hub
        self.destination_city = destination_city
        self.transport_mode = transport_mode
        self.cargo_category = cargo_category
        self.weight = weight_kg
        self.volume_cbm = volume_cbm
        self.distance = distance_km
        self.is_interstate = is_interstate
        self.priority_handling = priority_handling
        self.insurance_opted = insurance_opted
        self.declared_value = declared_value
        self.enterprise_account = enterprise_account

    def dimensional_weight(self):
        volumetric_weight = (self.volume_cbm * 1000) / 5

        return max(self.weight, volumetric_weight)

    def base_freight_rate_per_km(self):
        a = self.transport_mode

        if a == "Road Express":
            return 0.018

        elif a == "Rail Freight":
            return 0.0095

        elif a == "Air Cargo":
            return 0.055

        else:
            return 0

    def freight_cost(self):
        a = self.dimensional_weight()
        b = self.distance
        c = self.base_freight_rate_per_km()
        cost = (a * b * c)

        return cost

    def cargo_cost_per_kg(self):
        a = self.cargo_category

        if a == "Standard":
            return 0

        elif a == "Fragile":
            return 2.5

        elif a == "Perishable":
            return 4

        elif a == "Hazardous":
            return 8

        else:
            return 0

    def cargo_handling_surcharge(self):
        a = self.cargo_category
        b = self.dimensional_weight()
        c = self.cargo_cost_per_kg()

        if a == "Standard":
            fee = 0

        elif a == "Fragile":
            fee = 350

        elif a == "Perishable":
            fee = 600

        elif a == "Hazardous":
            fee = 1200

        else:
            fee = 0

        return (c * b) + fee

    def priority_dispatch_fee(self):
        a = self.priority_handling
        b = self.freight_cost()
        c = b * 0.15

        if a:
            return max(500, c)

        else:
            return 0

    def priority_dispatch_status(self):
        a = self.priority_handling

        if a:
            return "Is Activated."

        else:
            return "Not Opted."

    def insurance_premium(self):
        a = self.insurance_opted
        b = self.declared_value
        c = self.cargo_category
        d = b * 0.015
        e = b * 0.008

        if a and b > 0:

            if c in ("Hazardous", "Fragile"):
                return d

            else:
                return e 

    def insurance_status(self):
        a = self.insurance_opted

        if a:
            return "Is Activated"

        else:
            return "Not Opted"

    def fuel_surcharge_fee(self):
        a = self.freight_cost()
        b = self.fuel_surcharge_rate

        fuel_surcharge = a * b

        return fuel_surcharge

    def carbon_offset_fee(self):
        a = self.distance
        b = self.carbon_offset_fee_per_km

        carbon_offset_fee = a * b

        return carbon_offset_fee

    def gross_logistics_total(self):
        a = self.freight_cost()
        b = self.cargo_handling_surcharge()
        c = self.priority_dispatch_fee()
        d = self.fuel_surcharge_fee()
        e = self.carbon_offset_fee()

        gross_total = a + b + c + d + e

        return gross_total

    def enterprise_rebate(self):
        a = self.enterprise_account
        b = self.gross_logistics_total()

        if a:

            if b > 25000:
                rebate = 0.12

            elif b > 10000:
                rebate = 0.07

            else:
                rebate = 0.04

        else:
            rebate = 0

        return rebate * b

    def net_taxable_amount(self):
        a = self.gross_logistics_total()
        b = self.enterprise_rebate()

        taxable_amount = a - b

        return taxable_amount

    def calc_cgst(self):
        a = self.is_interstate
        b = self.base_cgst_rate
        c = self.net_taxable_amount()

        if a:
            cgst_rate = 0

        else:
            cgst_rate = b

        return cgst_rate * c

    def calc_sgst(self):
        a = self.is_interstate
        b = self.base_sgst_rate
        c = self.net_taxable_amount()

        if a:
            sgst_rate = 0

        else:
            sgst_rate = b

        return sgst_rate * c

    def calc_igst(self):
        a = self.base_igst_rate
        b = self.net_taxable_amount()
        igst = a * b

        return igst

    def total_tax(self):
        a = self.calc_cgst()
        b = self.calc_sgst()
        c = self.calc_igst()

        total_tax = a + b + c

        return total_tax

    def route(self):
        a = self.hub
        b = self.destination_city

        return f"From {a} --------> To {b}"

    def final_invoice_amount(self):
        a = self.net_taxable_amount()
        b = self.total_tax()

        total_amount = a + b

        return total_amount

    def account_type(self):
        a = self.enterprise_account

        if a:
            return "Enterprise Account"

        else:
            return "Personal Account"
        
    def generate_consignment_waybill(self):
        return f"""
{'\n' + '=' * 72}
{'EKART LOGISTICS':^72}
{'=' * 72}
{'CLIENT INFORMATION':^72}
{'-' * 72}
Client Name                        : {self.name}
Tracking ID                        : {self.tracking_id}
Account Type                       : {self.account_type()}
{'-' * 72}
{'SHIPPING INFORMATION':^72}
{'-' * 72}
Route                              : {self.route()}
Transport Mode                     : {self.transport_mode}
Distance                           : {self.distance} KM
{'-' * 72}
{'ITEM INFORMATION':^72}
{'-' * 72}
Actual Weight                      : {self.weight} KG
Volumetric Weight                  : {self.volume_cbm} Cubic Metre
Chargeable Weight                  : {self.dimensional_weight()} KG
Priority Handling                  : {self.priority_dispatch_status()}
Insurance Itemized                 : {self.insurance_status()}
{'-' * 72}
{'CHARGES BREAKDOWN':^72}
{'-' * 72}
Base Freight                       : ₹{self.freight_cost():>14,.2f}
Surcharges                         : ₹{self.cargo_handling_surcharge():>14,.2f}
Fuel Surcharge                     : ₹{self.fuel_surcharge_fee():>14,.2f}
Green Carbon Offset Fee            : ₹{self.carbon_offset_fee():>14,.2f}
{'-' * 72}
GROSS TOTAL                        : ₹{self.gross_logistics_total():>14,.2f}
{'-' * 72}
Enterprise Rebate                  : ₹{self.enterprise_rebate():>14,.2f}
Itemized GST :  i) CGST (9 %)      : ₹{self.calc_cgst():>14,.2f}
               ii) SGST (9 %)      : ₹{self.calc_sgst():>14,.2f}
              iii) IGST (18 %)     : ₹{self.calc_igst():>14,.2f}
{'-' * 72}
FINAL INVOICED AMOUNT              : ₹{self.final_invoice_amount():>14,.2f}
{'=' * 72}
{'THANK YOU!':^72}
{'=' * 72}\n\n\n
"""

class LogisticsFleetBatchProcessor:
    def __init__(self, batch_id : str, warehouse_location : str, consignments : list[ShipmentOrder] = []):
        self.batch_id = batch_id
        self.warehouse_location = warehouse_location
        self.consignments = consignments

    def add_consignment(self, order : ShipmentOrder):
        a = self.consignments
        a.append(order)

    def total_batch_weight(self):
        total_kg = 0

        for order in self.consignments:
            total_kg += order.dimensional_weight()

        total_tonnes = total_kg / 1000

        return total_tonnes

    def total_batch_revenue(self):
        total_revenue = 0

        for order in self.consignments:
            total_revenue += order.final_invoice_amount()

        return total_revenue

    def total_tax_collected(self):
        total_tax = 0

        for order in self.consignments:
            total_tax += order.total_tax()

        return total_tax

    def batch_dispatch_manifest(self):
        print(f"""
{'\n' * 10}
{'=' * 170}
{'\n' * 10}
{'=' * 72}
{'=' * 72}
{self.warehouse_location:^72}
{'=' * 72}
{'=' * 72}
""")
        for i, order in enumerate(self.consignments, start = 1):
            print(f"{i}:- {order.generate_consignment_waybill()}")

        total_consignments = len(self.consignments)
        total_tonnage = self.total_batch_weight()
        total_tax = self.total_tax_collected()
        grand_revenue = self.total_batch_revenue()

        print(f"""
{'=' * 72}
{'BATCH SUMMARY':^72}                           
{'=' * 72}
Batch ID                          : {self.batch_id}
Warehouse Location                : {self.warehouse_location}
{'-' * 72}
Total Consignments                : {total_consignments}
Total Tonnage                     : {total_tonnage:,.3f} Metric Ton
Total Tax                         : ₹{total_tax:>14,.2f}
{'-' * 72}
TOTAL INVOICED REVENUE            : ₹{grand_revenue:>14,.2f}
{'=' * 72}
{'THANK YOU!':^72}                            
{'=' * 72}
""")





if __name__ == "__main__":





    batch = LogisticsFleetBatchProcessor(
        "BATCH-MH-2026-09",
        "Central Logistics Hub - Pune"
    )




    orders = [
        ShipmentOrder(
            "TRK-9001",
            "Serum Pharma Ltd",
            "Pune",
            "Hyderabad",
            "Air Cargo",
            "Perishable",
            120.0,
            1.2,
            560.0,
            True,
            True,
            True,
            450000.0,
            True
        ),

        ShipmentOrder(
            "TRK-9002",
            "Bharat Heavy Industrial",
            "Pune",
            "Nagpur",
            "Rail Freight",
            "Hazardous",
            2400.0,
            4.8,
            720.0,
            False,
            False,
            True,
            1200000.0,
            True
        ),

        ShipmentOrder(
            "TRK-9003",
            "CraftGlass Studios",
            "Pune",
            "Mumbai",
            "Road Express",
            "Fragile",
            45.0,
            0.9,
            150.0,
            False,
            True,
            False,
            0.0,
            False
        ),

        ShipmentOrder(
            "TRK-9004",
            "OmniRetail Distribution",
            "Pune",
            "Bengaluru",
            "Road Express",
            "Standard",
            850.0,
            3.5,
            840.0,
            True,
            False,
            True,
            320000.0,
            False
        ),

        ShipmentOrder(
            "TRK-9005",
            "Adani Steels Distribution",
            "Pune",
            "Mengaluru",
            "Air Cargo",
            "Hazardous",
            1850.0,
            7.5,
            2400.0,
            False,
            True,
            True,
            32000.0,
            True
        ),

        ShipmentOrder(
            "TRK-9006",
            "Relaince Steel Distribution",
            "Pune",
            "Agra",
            "Air Cargo",
            "Hazardous",
            1850.0,
            9.5,
            1000.0,
            False,
            True,
            False,
            42000.0,
            True
        ),

        ShipmentOrder(
            "TRK-9007",
            "EastMan Solars",
            "Pune",
            "Delhi",
            "Rail Freight",
            "Perishable",
            1850.0,
            9.5,
            1200.0,
            False,
            True,
            True,
            70000.0,
            True
        ),

        ShipmentOrder(
            "TRK-9008",
            "UltraTech Cement",
            "Pune",
            "Agra",
            "Road Express",
            "Fragile",
            1900.0,
            10.5,
            5200.0,
            True,
            False,
            False,
            62000.0,
            False
        ),

        ShipmentOrder(
            "TRK-9009",
            "Blue Ways Corporation",
            "Pune",
            "Pakistan",
            "Air Cargo",
            "Hazardous",
            6000.0,
            50,
            4500.0,
            False,
            True,
            True,
            320000.0,
            False
        ),

        ShipmentOrder(
            "TRK-9010",
            "Ambuja Cement",
            "Pune",
            "Aurangabad",
            "Road Express",
            "Standard",
            5000.0,
            15.0,
            350.0,
            True,
            True,
            True,
            90000.0,
            True
        ),

        ShipmentOrder(
            "TRK-9011",
            "Luminous Solars",
            "Pune",
            "Chh. Sambhaji Nagar",
            "Rail Freight",
            "Fragile",
            6000.0,
            55.0,
            3500.0,
            True,
            False,
            True,
            900000.0,
            False
        ),

        ShipmentOrder(
            "TRK-9012",
            "Ambuja Cement",
            "Pune",
            "Chennai",
            "Air Cargo",
            "Perishable",
            9000.0,
            65.0,
            1550.0,
            False,
            True,
            True,
            90000.0,
            False
        ),
    ]



    for orders in orders:
        batch.add_consignment(orders)
        batch.batch_dispatch_manifest()