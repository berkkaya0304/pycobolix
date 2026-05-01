def main():
    print("--- FAST LANE AUTO REPAIR ---")
    license_plate = input("Vehicle License Plate: ")
    try:
        mileage = int(input("Current Mileage: "))
    except ValueError:
        mileage = 0

    oil_change = input("Oil Change ($45)? (Y/N): ").strip().upper() == 'Y'
    tire_rotate = input("Tire Rotation ($25)? (Y/N): ").strip().upper() == 'Y'
    inspection = input("State Inspection ($35)? (Y/N): ").strip().upper() == 'Y'
    try:
        labor_hours = float(input("Estimated Labor Hours ($80/hr): "))
    except ValueError:
        labor_hours = 0.0

    labor_cost = labor_hours * 80.00
    parts_cost = 0.0
    
    if oil_change:
        parts_cost += 45.00
        
    if tire_rotate:
        parts_cost += 25.00
        
    if inspection:
        parts_cost += 35.00
        
    total_estimate = labor_cost + parts_cost

    print("\n========================================")
    print("          SERVICE INVOICE               ")
    print("========================================")
    print(f"License: {license_plate} | Mileage: {mileage:06d}")
    print("----------------------------------------")
    if oil_change:
        print(" - Oil & Filter Replacement: $45.00")
    if tire_rotate:
        print(" - Tire Rotation:            $25.00")
    if inspection:
        print(" - State Safety Inspection:  $35.00")
    print("----------------------------------------")
    print(f"Total Parts/Services: ${parts_cost:7.2f}")
    print(f"Labor Cost:           ${labor_cost:7.2f}")
    print("========================================")
    print(f"FINAL ESTIMATE:       ${total_estimate:7.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
