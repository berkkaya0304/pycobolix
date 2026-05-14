class GymMembership:
    def __init__(self):
        self.init_fee = 50.00
        self.base_plan = 0.00
        self.pt_fee = 0.00
        self.discounts = 0.00
        self.total_pay = 0.00
        self.member_name = ""
        self.plan_type = ""
        self.trainer_req = ""

    def get_member(self):
        self.member_name = input("Enter New Member Name: ")
        self.plan_type = input("Plan Type (M=Monthly $40, Y=Yearly $400): ").upper()
        self.trainer_req = input("Add Personal Trainer (+$100/mo or $1000/yr)? (Y/N): ").upper()

    def calc_fees(self):
        self.discounts = 0.00
        self.pt_fee = 0.00
        self.init_fee = 50.00

        if self.plan_type == 'M':
            self.base_plan = 40.00
            if self.trainer_req == 'Y':
                self.pt_fee = 100.00
        elif self.plan_type == 'Y':
            self.base_plan = 400.00
            self.discounts = 50.00
            if self.trainer_req == 'Y':
                self.pt_fee = 1000.00
        else:
            self.base_plan = 40.00
            print("Invalid plan, defaulting to Monthly.")

        self.total_pay = self.init_fee + self.base_plan + self.pt_fee - self.discounts

    def show_contract(self):
        print("\n" + "=" * 46)
        print("      MEMBERSHIP AGREEMENT            ")
        print("=" * 46)
        print(f"Member: {self.member_name}")
        
        print(f"Initiation Fee:  ${self.init_fee:,.2f}")
        
        if self.discounts > 0:
            print(f"Promo Discount:  -${self.discounts:,.2f}")
        
        print(f"Plan Fee:        ${self.base_plan:,.2f}")
        
        if self.pt_fee > 0:
            print(f"Trainer Fee:     ${self.pt_fee:,.2f}")
        
        print("-" * 46)
        print(f"DUE TODAY:       ${self.total_pay:,.2f}")
        print("=" * 46)

def main():
    print("*** IRON FIT STUDIO REGISTRATION ***")
    while True:
        member = GymMembership()
        member.get_member()
        member.calc_fees()
        member.show_contract()
        
        run_loop = input("Register another member? (Y/N): ").upper()
        if run_loop != 'Y':
            break

if __name__ == "__main__":
    main()
