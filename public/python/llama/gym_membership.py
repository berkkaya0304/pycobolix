# GYM-MEMBERSHIP - Iron Fit Studio Registration
# Converted from COBOL to Python

def main():
    print("*** IRON FIT STUDIO REGISTRATION ***")
    run_loop = 'Y'
    while run_loop.upper() == 'Y':
        m_name = input("Enter New Member Name: ")
        plan_type = input("Plan Type (M=Monthly $40, Y=Yearly $400): ").strip().upper()
        trainer_req = input("Add Personal Trainer (+$100/mo or $1000/yr)? (Y/N): ").strip().upper()

        init_fee = 50.00
        discounts = 0.0
        pt_fee = 0.0

        if plan_type == 'M':
            base_plan = 40.00
            if trainer_req == 'Y':
                pt_fee = 100.00
        elif plan_type == 'Y':
            base_plan = 400.00
            discounts = 50.00
            if trainer_req == 'Y':
                pt_fee = 1000.00
        else:
            base_plan = 40.00
            print("Invalid plan, defaulting to Monthly.")

        total_pay = init_fee + base_plan + pt_fee - discounts

        print("")
        print("======================================")
        print("      MEMBERSHIP AGREEMENT            ")
        print("======================================")
        print(f"Member: {m_name}")
        print(f"Initiation Fee:  ${init_fee:,.2f}")
        if discounts > 0:
            print(f"Promo Discount:  -${discounts:,.2f}")
        print(f"Plan Fee:        ${base_plan:,.2f}")
        if pt_fee > 0:
            print(f"Trainer Fee:     ${pt_fee:,.2f}")
        print("--------------------------------------")
        print(f"DUE TODAY:       ${total_pay:,.2f}")
        print("======================================")

        run_loop = input("Register another member? (Y/N): ").strip()

if __name__ == "__main__":
    main()
