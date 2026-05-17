def main():
    print("--- SPARKLE MAIDS QUOTE ---")
    try:
        sq_footage = int(input("Approximate Sq Footage of house: "))
    except ValueError:
        sq_footage = 0
    has_pets = input("Do you have pets? (Y/N): ").strip().upper() == 'Y'
    deep_clean = input("Require initial deep clean? (Y/N): ").strip().upper() == 'Y'

    base_rate = sq_footage * 0.10
    pet_surcharge = 30.00 if has_pets else 0.0
    dc_surcharge = base_rate * 0.50 if deep_clean else 0.0

    total_quote = base_rate + pet_surcharge + dc_surcharge

    print("\n======================================")
    print("        CLEANING SERVICE QUOTE        ")
    print("======================================")
    print(f"Home Size: {sq_footage} sq ft.")
    print("--------------------------------------")
    print(f"Standard Cleaning Base: ${base_rate:6.2f}")
    
    if pet_surcharge > 0:
        print(f"Pet Hair/Dander Fee:    ${pet_surcharge:6.2f}")
        
    if dc_surcharge > 0:
        print(f"Initial Deep Clean Add: ${dc_surcharge:6.2f}")
        
    print("--------------------------------------")
    print(f"ESTIMATED TOTAL:        ${total_quote:6.2f}")
    print("======================================")

if __name__ == "__main__":
    main()
