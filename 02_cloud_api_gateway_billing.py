class APICallTransaction:
    gst_rate = 0.18
    burst_surcharge_rate = 0.004

    def __init__(self, request_id : str, tenant_id : str, tenant_tier : str, endpoint_route : str, total_calls : int, payload_processed_mb : float, avg_latency_ms : float, is_sla_guaranteed : bool = False, datacenter_region : str = "ap-south-1", custom_domain_ssl : bool = False):
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.tenant_tier = tenant_tier
        self.endpoint_route = endpoint_route
        self.total_calls = total_calls
        self.payload_processed_mb = payload_processed_mb
        self.avg_latency_ms = avg_latency_ms
        self.is_sla_guaranteed = is_sla_guaranteed
        self.datacenter_region = datacenter_region
        self.custom_domain_ssl = custom_domain_ssl

    def tier_quota_limit(self) -> int:
        t = self.tenant_tier

        if t == "Developer":
            max_calls_allowed = 10000

        elif t == "Team":
            max_calls_allowed = 100000

        elif t == "Enterprise":
            max_calls_allowed = 1000000

        else:
            max_calls_allowed = 0

        return max_calls_allowed

    def billable_calls(self) -> int:
        a = self.tier_quota_limit()
        b = self.total_calls

        if b > a:
            return b - a

        else:
            return 0

    def endpoint_unit_cost(self) -> float:
        r = self.endpoint_route

        if r == "/v1/auth":
            endpoint_cost = 0.002

        elif r == "/v1/data/query":
            endpoint_cost = 0.008

        elif r == "/v1/ai/infer":
            endpoint_cost = 0.045

        elif r == "/v1/export":
            endpoint_cost = 0.020

        else:
            endpoint_cost = 0.010

        return endpoint_cost

    def base_traffic_cost(self) -> float:
        return self.billable_calls() * self.endpoint_unit_cost()

    def bandwidth_charge(self) -> float:
        mb = self.payload_processed_mb

        if mb > 500:
            charge = (mb - 500) * 0.15

        else:
            charge = 0

        return charge

    def base_total(self):
        a = self.base_traffic_cost()
        b = self.bandwidth_charge()

        base_total = a + b

        return base_total

    def sla_and_latency_penalty(self) -> float:
        a = self.is_sla_guaranteed
        b = self.avg_latency_ms

        if a:
            enterprise_monitoring_fee = 500

            if b > 250:
                enterprise_monitoring_fee -= 150

            return max(0, enterprise_monitoring_fee)

        else:
            return 0

    def regional_multiplier(self) -> float:
        a = self.base_total()
        b = self.datacenter_region
        
        if b == "ap-south-1":
            cross_region_egress = 1.0

        elif b == "eu-west-1":
            cross_region_egress = 1.12

        elif b == "us-east-1":
            cross_region_egress = 1.08

        else:
            cross_region_egress = 1.0

        return a * cross_region_egress

    def custom_domain_fee(self):
        a = self.custom_domain_ssl

        if a:
            fee = 199

        else:
            fee = 0

        return fee

    def gross_invoice(self) -> float:
        a = self.regional_multiplier()
        b = self.sla_and_latency_penalty()
        c = self.custom_domain_fee()

        gross_total = a + b + c

        return gross_total

    def tier_volume_discount(self) -> float:
        a = self.tenant_tier
        b = self.gross_invoice()

        if a == "Enterprise":
            discount = 0.2

        elif a == "Team":
            discount = 0.1

        else:
            discount = 0 

        return b * discount

    def taxable_amount(self) -> float:
        a = self.gross_invoice()
        b = self.tier_volume_discount()

        taxable_amount = a - b

        return taxable_amount

    def gst(self) -> float:
        a = self.taxable_amount()
        b = self.gst_rate

        gst = a * b

        return gst

    def final_bill(self) -> float:
        a = self.taxable_amount()
        b = self.gst()

        total_amount = a + b

        return total_amount

    def sla_guarantee_status(self) -> str:
        a = self.is_sla_guaranteed

        if a:
            return "Yes! Sla Guaranteed."

        else:
            return "Not Guaranteed."

    def custom_domain_status(self) -> str:
        a = self.custom_domain_ssl

        if a:
            return "Custom Domain is selected."

        else:
            return "Not Selected."

    def api_billing_receipt(self) -> str:
        return f"""
{'=' * 80}
{'API GATEWAY METERED USAGE STATEMENT':^80}
{'=' * 80}
{'CLIENT INFO.':^80}
{'-' * 80}
Request ID                        : {self.request_id}
Tenant ID                         : {self.tenant_id}
Tier                              : {self.tenant_tier}
Region                            : {self.datacenter_region}
{'-' * 80}
{'OTHER INFO.':^80}
{'-' * 80}
Route Invocation                  : {self.endpoint_route}
Calls Logged                      : {self.total_calls:,.2f}
Included Calls Quota              : {self.tier_quota_limit():,.2f}
Billable Calls                    : {self.billable_calls():,.2f}
Data Processed                    : {self.payload_processed_mb:,.2f} MB
Avg. Latency                      : {self.avg_latency_ms}
SLA Guaranteed                    : {self.sla_guarantee_status()}
{'-' * 80}
{'CHARGES BREAKDOWN':^80}
{'-' * 80}
Base Traffic Cost                 : ₹{self.base_traffic_cost():>14,.2f}
Bandwidth Surcharge               : ₹{self.bandwidth_charge():>14,.2f}
{'-' * 80}
BASE TOTAL FEE                    : ₹{self.base_total():>14,.2f}
{'-' * 80}
FEE AFTER REGION MULTIPLIER       : ₹{self.regional_multiplier():>14,.2f}
{'-' * 80}
SLA & Latency Penalty             : ₹{self.sla_and_latency_penalty():>14,.2f}
Custom Domain FEE                 : ₹{self.custom_domain_fee():>14,.2f}
{'-' * 80}
GROSS CHARGES                     : ₹{self.gross_invoice():>14,.2f}
{'-' * 80}
Volume Rebate Applied             : ₹{self.tier_volume_discount():>14,.2f}
GST (18 %)                        : ₹{self.gst():>14,.2f}
{'-' * 80}
FINAL BALANCE DUE                 : ₹{self.final_bill():>14,.2f}
{'=' * 80}
{'THANK YOU!':^80}
{'=' * 80}
{'\n' * 6}
"""




class APIGatewayTenantManager:
    def __init__(self, gateway_cluster_name  : str, billing_month : str, transactions : list[APICallTransaction] = []):
        self.gateway_cluster_name = gateway_cluster_name
        self.billing_month = billing_month
        self.transactions = transactions

    def register_transaction(self, txn : APICallTransaction):
        a = self.transactions
        a.append(txn)

    def total_calls_served(self) -> int:
        total_calls = 0

        for txn in self.transactions:
            total_calls += txn.total_calls

        return total_calls

    def total_bandwidth_gb(self) -> float:
        total_bandwidth_mb = 0

        for txn in self.transactions:
            total_bandwidth_mb += txn.payload_processed_mb

        total_bandwidth_gb = (total_bandwidth_mb / 1024)

        return total_bandwidth_gb

    def total_perform_revenue(self) -> float:
        total_revenue = 0

        for txn in self.transactions:
            total_revenue += txn.final_bill()

        return total_revenue

    def total_gst_collected(self) -> float:
        total_gst = 0

        for txn in self.transactions:
            total_gst += txn.gst()

        return total_gst

    def gateway_audit_report(self) -> str:
        print(f"""
{'\n' * 10}
{'=' * 170}
{'\n' * 10}
{'=' * 80}
{'=' * 80}
{self.gateway_cluster_name:^80}
{'=' * 80}
{'=' * 80}
{'\n' * 10}
""")
        for i, txn in enumerate(self.transactions, start = 1):
            print(f"{i}:- {txn.api_billing_receipt()}")

        total_calls = self.total_calls_served()
        total_served_gb = self.total_bandwidth_gb()
        total_gst = self.total_gst_collected()
        total_revenue = self.total_perform_revenue()

        print(f"""
{'\n' * 5}
{'=' * 80}
{'EXECUTIVE API GATEWAY INFRASTRUCTURE AUDIT':^80}
{'=' * 80}
Gateway Cluster Name             : {self.gateway_cluster_name}
Billing Month                    : {self.billing_month}
{'-' * 80}
Total Cluster Calls              : {total_calls:,.2f}
Bandwidth Served In GB           : {total_served_gb:,.2f} GB
{'-' * 80}
Total GST Remitted               : ₹{total_gst:>14,.2f} 
Total Gateway Revenue            : ₹{total_revenue:>14,.2f}
{'=' * 80}
{'THANK YOU!':^80}
{'=' * 80}
""")









if __name__ == "__main__":





    gateway_cluster = APIGatewayTenantManager(
        "Github-Cluster-MH-20",
        "January"
    )





    clients = [
        APICallTransaction(
            "REQ-801",
            "TNT-Alpha", 
            "Enterprise", 
            "/v1/ai/infer", 
            1450000, 
            2800.0, 
            280.0, 
            True, 
            "ap-south-1", 
            True
        ),

        APICallTransaction(
            "REQ-802",
            "TNT-BetaDev",
            "Developer", 
            "/v1/auth",
            25000,
            320,
            90,
            False,
            "ap-south-1",
            False 
        ),

        APICallTransaction(
            "REQ-803",
            "TNT-CloudData",
            "Team",
            "/v1/data/query",
            180000,
            1200,
            310,
            True,
            "eu-west-1",
            True
        ),

        APICallTransaction(
            "REQ-804", 
            "TNT-FinReport", 
            "Team", 
            "/v1/export",
            95000,
            1850,
            140,
            False,
            "us-east-1",
            False
        ),

        APICallTransaction(
            "REQ-805", 
            "TNT-Sigma", 
            "Developer", 
            "/v1/ai/infer",
            75000,
            1950,
            540,
            True,
            "eu-west-1",
            True
        ),

        APICallTransaction(
            "REQ-806", 
            "TNT-CID", 
            "Enterprise", 
            "/v1/auth",
            500000,
            5550,
            340,
            True,
            "ap-south-1",
            False
        ),

        APICallTransaction(
            "REQ-807", 
            "TNT-Report", 
            "Developer", 
            "/v1/auth",
            195000,
            1750,
            240,
            False,
            "us-east-1",
            True
        ),

        APICallTransaction(
            "REQ-808", 
            "TNT-SBI", 
            "Team", 
            "/v1/ai/infer",
            195000,
            3900,
            145,
            False,
            "eu-west-1",
            False
        ),

        APICallTransaction(
            "REQ-809", 
            "TNT-Tetha", 
            "Enterprise", 
            "/v1/export",
            2995000,
            7850,
            240,
            False,
            "us-east-1",
            True
        ),

        APICallTransaction(
            "REQ-810", 
            "TNT-FinReport", 
            "Team", 
            "/v1/auth",
            95000,
            850,
            140,
            False,
            "ap-south-1",
            False
        ),

        APICallTransaction(
            "REQ-811", 
            "TNT-FinReport", 
            "Developer", 
            "/v1/ai/infer",
            995000,
            9850,
            1000,
            True,
            "eu-west-1",
            True
        ),       
    ]




    for clients in clients:
        gateway_cluster.register_transaction(clients)
        gateway_cluster.gateway_audit_report()