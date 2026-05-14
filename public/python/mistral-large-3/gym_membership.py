def gym_membership():
    print("*** IRON FIT STUDIO REGISTRATION ***")

    while True:
        member_name = input("Enter New Member Name: ").strip()

        while True:
            plan_type = input("Plan Type (M=Monthly $40, Y=Yearly $400): ").strip().upper()
            if plan_type in ('M', 'Y'):
                break
            print("Invalid plan, please enter M or Y.")

        trainer_req = input("Add Personal Trainer (+$100/mo or $1000/yr)? (Y/N): ").strip().upper()
        wants_pt = trainer_req == 'Y'

        init_fee = 50.00
        base_plan = 0.00
        pt_fee = 0.00
        discounts = 0.00

        if plan_type == 'M':
            base_plan = 40.00
            if wants_pt:
                pt_fee = 100.00
        elif plan_type == 'Y':
            base_plan = 400.00
            discounts = 50.00
            if wants_pt:
                pt_fee = 1000.00

        total_pay = init_fee + base_plan + pt_fee - discounts

        print("\n======================================")
        print("      MEMBERSHIP AGREEMENT            ")
        print("======================================")
        print(f"Member: {member_name}")
        print(f"Initiation Fee:  ${init_fee:,.2f}")

        if discounts > 0:
            print(f"Promo Discount:  -${discounts:,.2f}")

        print(f"Plan Fee:        ${base_plan:,.2f}")

        if pt_fee > 0:
            print(f"Trainer Fee:     ${pt_fee:,.2f}")

        print("--------------------------------------")
        print(f"DUE TODAY:       ${total_pay:,.2f}")
        print("======================================\n")

        another = input("Register another member? (Y/N): ").strip().upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    gym_membership()
