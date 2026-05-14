       IDENTIFICATION DIVISION.
       PROGRAM-ID. CAR-DEALER.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE-APP.
          05 BUYER-NAME      PIC X(30).
          05 BASE-MODEL      PIC 9.
             88 SEDAN        VALUE 1.
             88 SUV          VALUE 2.
             88 TRUCK        VALUE 3.
          05 TRIM-LEVEL      PIC 9.
             88 BASE-TRIM    VALUE 1.
             88 SPORT-TRIM   VALUE 2.
             88 LUXURY-TRIM  VALUE 3.
          05 DOWN-PAYMENT    PIC 9(6)V99.
          05 LOAN-MONTHS     PIC 9(3).

       01 VEHICLE-COST.
          05 BASE-PRICE      PIC 9(6)V99 VALUE ZERO.
          05 TRIM-UPCHARGE   PIC 9(5)V99 VALUE ZERO.
          05 TOTAL-VEH-PRICE PIC 9(6)V99 VALUE ZERO.
          
       01 FINANCING.
          05 FINANCED-AMT    PIC 9(6)V99.
          05 INTEREST-RATE   PIC 9V9999 VALUE 0.05.
          05 TOTAL-INTEREST  PIC 9(5)V99.
          05 TOTAL-PAYBACK   PIC 9(7)V99.
          05 MONTHLY-PAYMENT PIC 9(4)V99.

       01 D-FMT              PIC $ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-DEAL DESC.
           DISPLAY "--- PLATINUM AUTO SALES ---".
           DISPLAY "Buyer Name: ".
           ACCEPT BUYER-NAME.
           DISPLAY "Model (1=Sedan $25k, 2=SUV $35k, 3=Truck $45k): ".
           ACCEPT BASE-MODEL.
           DISPLAY "Trim (1=Base $0, 2=Sport $5k, 3=Luxury $10k): ".
           ACCEPT TRIM-LEVEL.
           DISPLAY "Down Payment Amount ($): ".
           ACCEPT DOWN-PAYMENT.
           DISPLAY "Loan Term (Months): ".
           ACCEPT LOAN-MONTHS.

           PERFORM PRICE-CALC.
           PERFORM FINANCE-CALC.
           PERFORM OUTPUT-SHEET.
           STOP RUN.

       PRICE-CALC.
           EVALUATE TRUE
               WHEN SEDAN
                   MOVE 25000.00 TO BASE-PRICE
               WHEN SUV
                   MOVE 35000.00 TO BASE-PRICE
               WHEN TRUCK
                   MOVE 45000.00 TO BASE-PRICE
               WHEN OTHER
                   MOVE 25000.00 TO BASE-PRICE
           END-EVALUATE.

           EVALUATE TRUE
               WHEN BASE-TRIM
                   MOVE ZERO TO TRIM-UPCHARGE
               WHEN SPORT-TRIM
                   MOVE 5000.00 TO TRIM-UPCHARGE
               WHEN LUXURY-TRIM
                   MOVE 10000.00 TO TRIM-UPCHARGE
               WHEN OTHER
                   MOVE ZERO TO TRIM-UPCHARGE
           END-EVALUATE.

           COMPUTE TOTAL-VEH-PRICE = BASE-PRICE + TRIM-UPCHARGE.

       FINANCE-CALC.
           COMPUTE FINANCED-AMT = TOTAL-VEH-PRICE - DOWN-PAYMENT.
           
           COMPUTE TOTAL-INTEREST = FINANCED-AMT * INTEREST-RATE 
                                  * (LOAN-MONTHS / 12).
                                  
           COMPUTE TOTAL-PAYBACK = FINANCED-AMT + TOTAL-INTEREST.
           COMPUTE MONTHLY-PAYMENT = TOTAL-PAYBACK / LOAN-MONTHS.

       OUTPUT-SHEET.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "       VEHICLE PURCHASE SHEET           "
           DISPLAY "========================================"
           DISPLAY "Buyer: " BUYER-NAME
           DISPLAY "----------------------------------------"
           MOVE BASE-PRICE TO D-FMT.
           DISPLAY "Base Price:       " D-FMT.
           MOVE TRIM-UPCHARGE TO D-FMT.
           DISPLAY "Trim Upcharge:    " D-FMT.
           MOVE TOTAL-VEH-PRICE TO D-FMT.
           DISPLAY "Total Vehicle:    " D-FMT.
           DISPLAY "----------------------------------------"
           MOVE DOWN-PAYMENT TO D-FMT.
           DISPLAY "Down Payment:    -" D-FMT.
           MOVE FINANCED-AMT TO D-FMT.
           DISPLAY "Amount Financed:  " D-FMT.
           DISPLAY "----------------------------------------"
           MOVE MONTHLY-PAYMENT TO D-FMT.
           DISPLAY "EST. MONTHLY PMT: " D-FMT.
           DISPLAY "========================================".
