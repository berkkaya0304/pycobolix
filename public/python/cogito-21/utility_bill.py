class UtilityBill:
    def __init__(self):
        self.account_info = {
            'account_number': '',
            'customer_name': ''
        }
        self.usage_data = {
            'electricity_kwh': 0,
            'water_gallons': 0
        }
        self.bill_calcs = {
            'electricity_base': 20.00,
            'electricity_charge': 0.00,
            'water_base': 15.00,
            'water_charge': 0.00,
            'total_charge': 0.00,
            'late_fee': 10.00,
            'include_late': False,
            'final_due': 0.00
        }

    def get_input(self):
        print("--- CITY UTILITIES BILLING ---")
        self.account_info['account_number'] = input("Account Number: ")
        self.account_info['customer_name'] = input("Customer Name: ")
        
        while True:
            try:
                self.usage_data['electricity_kwh'] = int(input("Electricity Used (kWh): "))
                self.usage_data['water_gallons'] = int(input("Water Used (Gallons): "))
                break
            except ValueError:
                print("Please enter valid numbers for usage.")
        
        late_input = input("Apply late fee? (Y/N): ").strip().upper()
        self.bill_calcs['include_late'] = late_input == 'Y'

    def calculate_charges(self):
        kwh = self.usage_data['electricity_kwh']
        if kwh <= 500:
            self.bill_calcs['electricity_charge'] = kwh * 0.12
        else:
            self.bill_calcs['electricity_charge'] = (500 * 0.12) + ((kwh - 500) * 0.15)
        
        self.bill_calcs['water_charge'] = (self.usage_data['water_gallons'] / 100) * 0.25
        
        self.bill_calcs['total_charge'] = (
            self.bill_calcs['electricity_base'] + 
            self.bill_calcs['electricity_charge'] + 
            self.bill_calcs['water_base'] + 
            self.bill_calcs['water_charge']
        )
        
        if not self.bill_calcs['include_late']:
            self.bill_calcs['late_fee'] = 0.00
        
        self.bill_calcs['final_due'] = self.bill_calcs['total_charge'] + self.bill_calcs['late_fee']

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def output_invoice(self):
        print("\n" + "*" * 40)
        print("        MONTHLY UTILITY BILL            ")
        print("*" * 40)
        print(f"Account: {self.account_info['account_number']}")
        print(f"Name:    {self.account_info['customer_name']}")
        print("-" * 40)
        
        print(f"ELEC Base Fee:       {self.format_currency(self.bill_calcs['electricity_base'])}")
        print(f"ELEC Usage Charge:   {self.format_currency(self.bill_calcs['electricity_charge'])}")
        print(f"  (Usage: {self.usage_data['electricity_kwh']} kWh)")
        print("-" * 40)
        
        print(f"WATER Base Fee:      {self.format_currency(self.bill_calcs['water_base'])}")
        print(f"WATER Usage Charge:  {self.format_currency(self.bill_calcs['water_charge'])}")
        print(f"  (Usage: {self.usage_data['water_gallons']} gals)")
        print("-" * 40)
        
        if self.bill_calcs['late_fee'] > 0:
            print(f"Prior Bal Late Fee:  {self.format_currency(self.bill_calcs['late_fee'])}")
        
        print(f"TOTAL AMOUNT DUE:    {self.format_currency(self.bill_calcs['final_due'])}")
        print("*" * 40)

def main():
    bill = UtilityBill()
    bill.get_input()
    bill.calculate_charges()
    bill.output_invoice()

if __name__ == "__main__":
    main()
