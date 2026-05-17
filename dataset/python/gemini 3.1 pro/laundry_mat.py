def main():
    print("--- SUDS & BUBBLES COIN LAUNDRY ---")
    try:
        wash_loads = int(input("Number of Washing Machines Needed: "))
    except ValueError:
        wash_loads = 0
    wash_temp = input("Wash Temp (1=Cold $3, 2=Warm $3.50, 3=Hot $4): ").strip()
    try:
        dryer_mins = int(input("Total Dryer Minutes ($0.25 per 5 mins): "))
    except ValueError:
        dryer_mins = 0
    try:
        buy_soap = int(input("Detergent Pods to Purchase ($1.50 ea): "))
    except ValueError:
        buy_soap = 0

    if wash_temp == '1':
        wash_rate = 3.00
    elif wash_temp == '2':
        wash_rate = 3.50
    elif wash_temp == '3':
        wash_rate = 4.00
    else:
        wash_rate = 3.00

    wash_tot = wash_loads * wash_rate
    dryer_tot = (dryer_mins // 5) * 0.25
    soap_tot = buy_soap * 1.50

    grand_tot = wash_tot + dryer_tot + soap_tot

    print("\n========================================")
    print("           LAUNDRY KIOSK TICKET         ")
    print("========================================")
    
    if wash_loads > 0:
        print(f"Washers ({wash_loads}):           ${wash_tot:6.2f}")
        
    if dryer_mins > 0:
        print(f"Dryer Time ({dryer_mins}m):        ${dryer_tot:6.2f}")
        
    if buy_soap > 0:
        print(f"Detergent Pods ({buy_soap}):      ${soap_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL INSERT COINS:     ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
