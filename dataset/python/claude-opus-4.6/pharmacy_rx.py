"""
Pharmacy Prescription System
Converted from COBOL (pharmacy_rx.cbl) to Python
"""


def main():
    print("--- MEDPLUS PHARMACY RX ---")
    pat_name = input("Patient Name: ")
    rx_number = input("Rx Prescription Number: ")
    drug_name = input("Medication Name: ")
    drug_qty = int(input("Quantity Dispensed: "))
    unit_cost = float(input("Unit Cost ($): "))
    has_insurance = input("Insurance on file? (Y/N): ").strip().upper()

    drug_total = drug_qty * unit_cost
    dispensing_fee = 5.00

    if has_insurance == "Y":
        copay_pct = 0.20
        insurance_pays = drug_total * (1 - copay_pct)
        patient_pays = drug_total * copay_pct + dispensing_fee
    else:
        insurance_pays = 0.0
        patient_pays = drug_total + dispensing_fee

    print()
    print("=========================================")
    print("          PRESCRIPTION RECEIPT            ")
    print("=========================================")
    print(f"Patient: {pat_name}")
    print(f"Rx#: {rx_number}")
    print(f"Drug: {drug_name} (x{drug_qty})")
    print("-----------------------------------------")
    print(f"Medication Cost:   ${drug_total:>12,.2f}")
    print(f"Dispensing Fee:    ${dispensing_fee:>12,.2f}")
    if has_insurance == "Y":
        print(f"Insurance Covers: -${insurance_pays:>11,.2f}")
    print("-----------------------------------------")
    print(f"PATIENT PAYS:      ${patient_pays:>12,.2f}")
    print("=========================================")


if __name__ == "__main__":
    main()
