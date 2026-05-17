def main():
    print("--- GATOR GOLF ADVENTURE ---")
    try:
        adult_qty = int(input("Number of Adults: "))
    except ValueError:
        adult_qty = 0
    try:
        child_qty = int(input("Number of Children (Under 12): "))
    except ValueError:
        child_qty = 0
    course_type = input("Course (1=9 Holes, 2=18 Holes): ").strip()

    if course_type == '1':
        adult_rate = 12.00
        child_rate = 8.00
    elif course_type == '2':
        adult_rate = 18.00
        child_rate = 12.00
    else:
        adult_rate = 12.00
        child_rate = 8.00

    adult_tot = adult_qty * adult_rate
    child_tot = child_qty * child_rate
    
    grand_tot = adult_tot + child_tot

    print("\n========================================")
    print("           MINI GOLF RECEIPT            ")
    print("========================================")
    
    if course_type == '2':
        print("Course Selected: 18-Hole Adventure")
    else:
        print("Course Selected: 9-Hole Quick Run")
        
    print("----------------------------------------")
    
    if adult_qty > 0:
        print(f"{adult_qty:02d}x Adult Tickets:   ${adult_tot:6.2f}")
    if child_qty > 0:
        print(f"{child_qty:02d}x Child Tickets:   ${child_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:  ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
