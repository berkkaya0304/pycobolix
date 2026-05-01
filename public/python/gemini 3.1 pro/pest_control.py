def main():
    print("--- BUG BUSTERS EXTERMINATING ---")
    client_name = input("Property Owner: ")
    try:
        sq_footage = int(input("Square Footage of Property: "))
    except ValueError:
        sq_footage = 0
    pest_type = input("Pest (1=Insects, 2=Rodent +$50, 3=Termite +$200):").strip()
    sub_monthly = input("Enroll in Monthly Plan (20% Off)? (Y/N): ").strip().upper() == 'Y'

    base_sqft = 0.05
    area_charge = sq_footage * base_sqft

    if pest_type == '1':
        pest_surchg = 0.0
    elif pest_type == '2':
        pest_surchg = 50.00
    elif pest_type == '3':
        pest_surchg = 200.00
    else:
        pest_surchg = 0.0

    gross_amt = area_charge + pest_surchg

    sub_discount = 0.0
    if sub_monthly:
        sub_discount = gross_amt * 0.20

    final_due = gross_amt - sub_discount

    print("\n========================================")
    print("           SERVICE INVOICE              ")
    print("========================================")
    print(f"Property: {client_name} ({sq_footage} sqft)")
    print("----------------------------------------")
    print(f"Property Area Charge:${area_charge:6.2f}")
    
    if pest_surchg > 0:
        print(f"Target Pest Surcharge: ${pest_surchg:6.2f}")
        
    if sub_monthly:
        print(f"Service Plan Disc:  -${sub_discount:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL TREATMENT:      ${final_due:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
