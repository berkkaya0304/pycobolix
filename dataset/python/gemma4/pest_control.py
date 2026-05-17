def main():
    print("--- BUG BUSTERS EXTERMINATING ---")
    
    client_name = input("Property Owner: ")
    try:
        sq_footage = int(input("Square Footage of Property: "))
        pest_type = int(input("Pest (1=Insects, 2=Rodent +$50, 3=Termite +$200): "))
    except ValueError:
        print("Invalid numeric input.")
        return

    sub_monthly = input("Enroll in Monthly Plan (20% Off)? (Y/N): ").strip().upper()

    base_sqft_rate = 0.05
    area_charge = sq_footage * base_sqft_rate

    pest_surcharges = {
        1: 0.00,   # Insects
        2: 50.00,  # Rodents
        3: 200.00  # Termites
    }
    pest_surchg = pest_surcharges.get(pest_type, 0.00)

    gross_amt = area_charge + pest_surchg
    
    sub_discount = 0.00
    if sub_monthly == 'Y':
        sub_discount = gross_amt * 0.20

    final_due = gross_amt - sub_discount

    print("\n========================================")
    print("           SERVICE INVOICE              ")
    print("========================================")
    print(f"Property: {client_name} ({sq_footage} sqft)")
    print("----------------------------------------")
    print(f"Property Area Charge: ${area_charge:,.2f}")
    
    if pest_surchg > 0:
        print(f"Target Pest Surcharge: ${pest_surchg:,.2f}")
        
    if sub_monthly == 'Y':
        print(f"Service Plan Disc:  -${sub_discount:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL TREATMENT:      ${final_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
