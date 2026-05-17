"""
Eight Ball Billiards Lounge
Converted from COBOL (billiards_club.cbl) to Python
"""


def main():
    print("--- EIGHT BALL BILLIARDS LOUNGE ---")
    table_num = input("Table Number: ")
    hours_played = float(input("Hours Played (e.g. 1.5): "))
    day_of_week = int(input("Day Rate (1=Weekday $12/h, 2=Weekend $18/h): "))
    snacks_tab = float(input("Snacks / Bar Tab Total ($): "))

    hourly_rate = 12.00 if day_of_week == 1 else 18.00

    table_cost = hours_played * hourly_rate
    total_chg = table_cost + snacks_tab

    print()
    print("========================================")
    print("           TABLE TAB RECEIPT            ")
    print("========================================")
    print(f"Table: {table_num}")
    print(f"Time:  {hours_played} hours")
    print("----------------------------------------")
    print(f"Hourly Rate Applied: ${hourly_rate:>9,.2f}")
    print(f"Table Bill:          ${table_cost:>9,.2f}")
    if snacks_tab > 0:
        print(f"Lounge / Bar Tab:    ${snacks_tab:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_chg:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
