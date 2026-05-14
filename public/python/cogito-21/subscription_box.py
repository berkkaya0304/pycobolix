class SubscriptionBox:
    def __init__(self):
        self.subscriber_name = ""
        self.tier_level = 0
        self.extra_snacks = False
        self.extra_gear = False
        self.base_price = 0.0
        self.addon_price = 0.0
        self.shipping = 5.0
        self.monthly_total = 0.0
        self.annual_total = 0.0

    def get_input(self):
        print("--- GEEK CRATE SUBSCRIPTION ---")
        self.subscriber_name = input("Subscriber Name: ")
        
        while True:
            try:
                self.tier_level = int(input("Tier (1=Basic $20, 2=Pro $40, 3=Elite $75): "))
                if self.tier_level not in (1, 2, 3):
                    print("Invalid tier, defaulted to Basic.")
                    self.tier_level = 1
                break
            except ValueError:
                print("Please enter a valid number (1, 2, or 3).")
        
        self.extra_snacks = input("Add Snack Pack ($10/mo)? (Y/N): ").upper() == 'Y'
        self.extra_gear = input("Add Premium Gear ($25/mo)? (Y/N): ").upper() == 'Y'

    def calculate_fees(self):
        if self.tier_level == 1:
            self.base_price = 20.0
        elif self.tier_level == 2:
            self.base_price = 40.0
        elif self.tier_level == 3:
            self.base_price = 75.0
            self.shipping = 0.0
        
        if self.extra_snacks:
            self.addon_price += 10.0
        if self.extra_gear:
            self.addon_price += 25.0
        
        self.monthly_total = self.base_price + self.addon_price + self.shipping
        self.annual_total = self.monthly_total * 12

    def print_summary(self):
        print("\n=======================================")
        print("      SUBSCRIPTION ENROLLMENT          ")
        print("=======================================")
        print(f"Welcome, {self.subscriber_name}!")
        print("---------------------------------------")
        print(f"Monthly Base Box:   ${self.base_price:,.2f}")
        
        if self.addon_price > 0:
            print(f"Monthly Add-ons:    ${self.addon_price:,.2f}")
        
        print(f"Shipping Fee:       ${self.shipping:,.2f}")
        print("---------------------------------------")
        print(f"TOTAL MONTHLY CHARGE: ${self.monthly_total:,.2f}")
        print(f"EST. ANNUAL COST:     ${self.annual_total:,.2f}")
        print("=======================================")

    def run(self):
        self.get_input()
        self.calculate_fees()
        self.print_summary()

if __name__ == "__main__":
    subscription = SubscriptionBox()
    subscription.run()
