def main():
    print("--- GATOR GOLF ADVENTURE ---")
    
    try:
        adult_qty = int(input("Number of Adults: "))
        child_qty = int(input("Number of Children (Under 12): "))
        course_type = int(input("Course (1=9 Holes, 2=18 Holes): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if course_type == 1:
        adult_rate = 12.00
        child_rate = 8.00
        course_name = "9-Hole Quick Run"
    elif course_type == 2:
        adult_rate = 18.00
        child_rate = 12.00
        course_name = "18-Hole Adventure"
    else:
        print("Invalid course selection. Defaulting to 9 holes.")
        adult_rate = 12.00
        child_rate = 8.00
        course_name = "9-Hole Quick Run"

    adult_tot = adult_qty * adult_rate
    child_tot = child_qty * child_rate
    grand_tot = adult_tot + child_tot

    print("\n" + "=" * 40)
    print("           MINI GOLF RECEIPT            ")
    print("=" * 40)
    print(f"Course Selected: {course_name}")
    print("-" * 40)
    
    if adult_qty > 0:
        print(f"{adult_qty}x Adult Tickets:   ${adult_tot:,.2f}")
    if child_qty > 0:
        print(f"{child_qty}x Child Tickets:   ${child_tot:,.2f}")
    
    print("-" * 40)
    print(f"TOTAL AMOUNT DUE:  ${grand_tot:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
