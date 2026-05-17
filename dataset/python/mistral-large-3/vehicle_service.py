def main_garage():
    print("--- FAST LANE AUTO REPAIR ---")

    license_plate = input("Vehicle License Plate: ").strip()
    mileage = int(input("Current Mileage: ").strip())

    oil_change = input("Oil Change ($45)? (Y/N): ").strip().upper()
    tire_rotate = input("Tire Rotation ($25)? (Y/N): ").strip().upper()
    inspection = input("State Inspection ($35)? (Y/N): ").strip().upper()
    labor_hours = float(input("Estimated Labor Hours ($80/hr): ").strip())

    labor_cost, parts_cost, total_estimate = calc_estimate(labor_hours, oil_change, tire_rotate, inspection)
    print_invoice(license_plate, mileage, oil_change, tire_rotate, inspection, parts_cost, labor_cost, total_estimate)

def calc_estimate(labor_hours, oil_change, tire_rotate, inspection):
    labor_cost = labor_hours * 80.00
    parts_cost = 0.0

    if oil_change == 'Y':
        parts_cost += 45.00
    if tire_rotate == 'Y':
        parts_cost += 25.00
    if inspection == 'Y':
        parts_cost += 35.00

    total_estimate = labor_cost + parts_cost
    return labor_cost, parts_cost, total_estimate

def print_invoice(license_plate, mileage, oil_change, tire_rotate, inspection, parts_cost, labor_cost, total_estimate):
    print("\n========================================")
    print("          SERVICE INVOICE               ")
    print("========================================")
    print(f"License: {license_plate} | Mileage: {mileage}")
    print("----------------------------------------")

    if oil_change == 'Y':
        print(" - Oil & Filter Replacement: $45.00")
    if tire_rotate == 'Y':
        print(" - Tire Rotation:            $25.00")
    if inspection == 'Y':
        print(" - State Safety Inspection:  $35.00")

    print("----------------------------------------")
    print(f"Total Parts/Services: ${parts_cost:,.2f}")
    print(f"Labor Cost:           ${labor_cost:,.2f}")
    print("========================================")
    print(f"FINAL ESTIMATE:       ${total_estimate:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main_garage()
