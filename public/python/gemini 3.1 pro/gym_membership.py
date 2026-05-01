def main():
    print("*** IRON FIT STUDIO REGISTRATION ***")
    run_loop = 'Y'
    
    while run_loop in ('Y', 'y'):
        m_name = input("Enter New Member Name: ")
        plan_type = input("Plan Type (M=Monthly $40, Y=Yearly $400): ").strip().upper()
        trainer_req = input("Add Personal Trainer (+$100/mo or $1000/yr)? (Y/N): ").strip().upper() == 'Y'

        init_fee = 50.00
        discounts = 0.0
        pt_fee = 0.0
        
        if plan_type == 'M':
            base_plan = 40.00
            if trainer_req:
                pt_fee = 100.00
        elif plan_type == 'Y':
            base_plan = 400.00
            discounts = 50.00
            if trainer_req:
                pt_fee = 1000.00
        else:
            base_plan = 40.00
            print("Invalid plan, defaulting to Monthly.")

        total_pay = init_fee + base_plan + pt_fee - discounts

        print("\n======================================")
        print("      MEMBERSHIP AGREEMENT            ")
        print("======================================")
        print(f"Member: {m_name}")
        print(f"Initiation Fee:  ${init_fee:6.2f}")
        
        if discounts > 0:
            print(f"Promo Discount:  -${discounts:6.2f}")
            
        print(f"Plan Fee:        ${base_plan:6.2f}")
        
        if pt_fee > 0:
            print(f"Trainer Fee:     ${pt_fee:6.2f}")
            
        print("--------------------------------------")
        print(f"DUE TODAY:       ${total_pay:6.2f}")
        print("======================================")

        run_loop = input("Register another member? (Y/N): ").strip()

if __name__ == "__main__":
    main()
