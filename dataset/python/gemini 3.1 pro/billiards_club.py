def main():
    print("--- EIGHT BALL BILLIARDS LOUNGE ---")
    table_num = input("Table Number: ")
    try:
        hours_played = float(input("Hours Played (e.g. 1.5): "))
    except ValueError:
        hours_played = 0.0
    day_of_week = input("Day Rate (1=Weekday $12/h, 2=Weekend $18/h): ").strip()
    try:
        snacks_tab = float(input("Snacks / Bar Tab Total ($): "))
    except ValueError:
        snacks_tab = 0.0

    if day_of_week == '1':
        hourly_rate = 12.00
    else:
        hourly_rate = 18.00

    table_cost = hours_played * hourly_rate
    total_chg = table_cost + snacks_tab

    print("\n========================================")
    print("           TABLE TAB RECEIPT            ")
    print("========================================")
    print(f"Table: {table_num}")
    print(f"Time:  {hours_played} hours")
    print("----------------------------------------")
    print(f"Hourly Rate Applied: ${hourly_rate:6.2f}")
    print(f"Table Bill:          ${table_cost:6.2f}")
    
    if snacks_tab > 0:
        print(f"Lounge / Bar Tab:    ${snacks_tab:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_chg:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
