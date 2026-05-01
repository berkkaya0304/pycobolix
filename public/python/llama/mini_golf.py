# MINI-GOLF - Gator Golf Adventure
# Converted from COBOL to Python

def main():
    print("--- GATOR GOLF ADVENTURE ---")
    adult_qty = int(input("Number of Adults: "))
    child_qty = int(input("Number of Children (Under 12): "))
    course_type = int(input("Course (1=9 Holes, 2=18 Holes): "))

    if course_type == 2:
        adult_rate = 18.00
        child_rate = 12.00
        course_name = "18-Hole Adventure"
    else:
        adult_rate = 12.00
        child_rate = 8.00
        course_name = "9-Hole Quick Run"

    adult_tot = adult_qty * adult_rate
    child_tot = child_qty * child_rate
    grand_tot = adult_tot + child_tot

    print("")
    print("========================================")
    print("           MINI GOLF RECEIPT            ")
    print("========================================")
    print(f"Course Selected: {course_name}")
    print("----------------------------------------")
    if adult_qty > 0:
        print(f"{adult_qty}x Adult Tickets:   ${adult_tot:,.2f}")
    if child_qty > 0:
        print(f"{child_qty}x Child Tickets:   ${child_tot:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:  ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
