# PEST-CONTROL - Bug Busters Exterminating
# Converted from COBOL to Python

def main():
    BASE_SQFT = 0.05

    print("--- BUG BUSTERS EXTERMINATING ---")
    client_name = input("Property Owner: ")
    sq_footage = int(input("Square Footage of Property: "))
    pest_type = int(input("Pest (1=Insects, 2=Rodent +$50, 3=Termite +$200):"))
    sub_monthly = input("Enroll in Monthly Plan (20% Off)? (Y/N): ").strip().upper()

    area_charge = sq_footage * BASE_SQFT

    if pest_type == 1:
        pest_surchg = 0.0
    elif pest_type == 2:
        pest_surchg = 50.00
    elif pest_type == 3:
        pest_surchg = 200.00
    else:
        pest_surchg = 0.0

    gross_amt = area_charge + pest_surchg
    sub_discount = gross_amt * 0.20 if sub_monthly == 'Y' else 0.0
    final_due = gross_amt - sub_discount

    print("")
    print("========================================")
    print("           SERVICE INVOICE              ")
    print("========================================")
    print(f"Property: {client_name} ({sq_footage} sqft)")
    print("----------------------------------------")
    print(f"Property Area Charge:${area_charge:,.2f}")
    if pest_surchg > 0:
        print(f"Target Pest Surcharge: ${pest_surchg:,.2f}")
    if sub_monthly == 'Y':
        print(f"Service Plan Disc:  -${sub_discount:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL TREATMENT:      ${final_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
