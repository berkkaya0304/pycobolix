def main():
    print("--- GLOBAL COURIER LOGISTICS ---")
    sender_name = input("Sender Name: ")
    try:
        weight_kg = float(input("Package Weight (kg): "))
    except ValueError:
        weight_kg = 0.0
    try:
        dim_length = int(input("Length (cm): "))
    except ValueError:
        dim_length = 0
    try:
        dim_width = int(input("Width (cm): "))
    except ValueError:
        dim_width = 0
    try:
        dim_height = int(input("Height (cm): "))
    except ValueError:
        dim_height = 0
    zone_code = input("Zone (1=Local, 2=Regional, 3=National): ").strip()

    volumetric_wt = (dim_length * dim_width * dim_height) / 5000.0
    
    if volumetric_wt > weight_kg:
        chargeable_wt = volumetric_wt
    else:
        chargeable_wt = weight_kg

    if zone_code == '1':
        zone_multiplier = 1.25
    elif zone_code == '2':
        zone_multiplier = 2.50
    elif zone_code == '3':
        zone_multiplier = 4.00
    else:
        zone_multiplier = 4.00
        print("Unknown zone. Defaulting to National.")

    base_shipping = chargeable_wt * zone_multiplier
    base_shipping += 5.00

    print("\n====================================")
    print("         SHIPPING MANIFEST          ")
    print("====================================")
    print(f"Sender: {sender_name}")
    print(f"Zone:   {zone_code}")
    print("------------------------------------")
    print(f"Actual Weight:     {weight_kg:.2f} kg")
    print(f"Volumetric Weight: {volumetric_wt:.2f} kg")
    print(f"Chargeable Weight: {chargeable_wt:.2f} kg")
    print("------------------------------------")
    print(f"TOTAL POSTAGE:     ${base_shipping:6.2f}")
    print("====================================")

if __name__ == "__main__":
    main()
