def main():
    print("--- EIGHT BALL BILLIARDS LOUNGE ---")
    
    try:
        table_num = int(input("Table Number: "))
        hours_played = float(input("Hours Played (e.g. 1.5): "))
        day_of_week = int(input("Day Rate (1=Weekday $12/h, 2=Weekend $18/h): "))
        snacks_tab = float(input("Snacks / Bar Tab Total ($): "))
        
        if day_of_week == 1:
            hourly_rate = 12.00
        else:
            hourly_rate = 18.00
            
        table_cost = hours_played * hourly_rate
        total_charge = table_cost + snacks_tab
        
        print("\n" + "=" * 40)
        print("           TABLE TAB RECEIPT            ")
        print("=" * 40)
        print(f"Table: {table_num}")
        print(f"Time:  {hours_played} hours")
        print("-" * 40)
        print(f"Hourly Rate Applied: ${hourly_rate:.2f}")
        print(f"Table Bill:          ${table_cost:.2f}")
        
        if snacks_tab > 0:
            print(f"Lounge / Bar Tab:    ${snacks_tab:.2f}")
            
        print("-" * 40)
        print(f"TOTAL AMOUNT DUE:    ${total_charge:.2f}")
        print("=" * 40)
        
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
