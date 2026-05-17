def main():
    print("--- GLOBAL VOICES TUTORING ---")
    
    student_name = input("Student Name: ")
    
    print("Language (1=Spanish $30/hr, 2=French $35/hr, 3=Mandarin $45/hr): ")
    try:
        lang_chosen = int(input())
    except ValueError:
        lang_chosen = 0

    print("Level (1=Beginner, 2=Advanced +$10/hr): ")
    try:
        level_tier = int(input())
    except ValueError:
        level_tier = 1

    try:
        hours_req = float(input("Hours per week requested: "))
    except ValueError:
        hours_req = 0.0

    # Determine Base Hourly Rate
    if lang_chosen == 1:
        base_hourly = 30.00
    elif lang_chosen == 2:
        base_hourly = 35.00
    elif lang_chosen == 3:
        base_hourly = 45.00
    else:
        base_hourly = 30.00

    # Determine Level Surcharge
    level_surchg = 10.00 if level_tier == 2 else 0.00

    # Calculations
    final_hourly = base_hourly + level_surchg
    total_cost = hours_req * final_hourly
    
    discount = 0.0
    if hours_req >= 5.0:
        discount = total_cost * 0.10
        
    net_payable = total_cost - discount

    # Output Invoice
    print("\n========================================")
    print("          TUTORING INVOICE              ")
    print("========================================")
    print(f"Student: {student_name}")
    print(f"Hours:   {hours_req:.1f} / week")
    print("----------------------------------------")
    print(f"Hourly Rate Applied: ${final_hourly:,.2f}")
    print(f"Gross Weekly Cost:   ${total_cost:,.2f}")
    
    if discount > 0:
        print(f"Volume Discount:    -${discount:,.2f}")
        
    print("----------------------------------------")
    print(f"NET WEEKLY PAYABLE:  ${net_payable:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
