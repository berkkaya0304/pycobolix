       IDENTIFICATION DIVISION.
       PROGRAM-ID. SUBSCRIPTION-BOX.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SUBSCRIBER-INFO.
          05 SUB-NAME        PIC X(25).
          05 TIER-LEVEL      PIC 9.
             88 BASIC-TIER   VALUE 1.
             88 PRO-TIER     VALUE 2.
             88 ELITE-TIER   VALUE 3.
          05 EXTRA-SNACKS    PIC X.
             88 ADD-SNACKS   VALUE 'Y'.
          05 EXTRA-GEAR      PIC X.
             88 ADD-GEAR     VALUE 'Y'.

       01 COSTS.
          05 BASE-PRICE      PIC 9(3)V99 VALUE ZERO.
          05 ADDON-PRICE     PIC 9(3)V99 VALUE ZERO.
          05 SHIPPING        PIC 9(2)V99 VALUE 5.00.
          05 MONTHLY-TOTAL   PIC 9(4)V99 VALUE ZERO.
          05 ANNUAL-TOTAL    PIC 9(5)V99 VALUE ZERO.

       01 F-CURR             PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-SUB.
           DISPLAY "--- GEEK CRATE SUBSCRIPTION ---".
           DISPLAY "Subscriber Name: ".
           ACCEPT SUB-NAME.
           DISPLAY "Tier (1=Basic $20, 2=Pro $40, 3=Elite $75): ".
           ACCEPT TIER-LEVEL.
           DISPLAY "Add Snack Pack ($10/mo)? (Y/N): ".
           ACCEPT EXTRA-SNACKS.
           DISPLAY "Add Premium Gear ($25/mo)? (Y/N): ".
           ACCEPT EXTRA-GEAR.

           PERFORM CALCULATE-FEES.
           PERFORM PRINT-SUMMARY.
           STOP RUN.

       CALCULATE-FEES.
           EVALUATE TRUE
               WHEN BASIC-TIER
                   MOVE 20.00 TO BASE-PRICE
               WHEN PRO-TIER
                   MOVE 40.00 TO BASE-PRICE
               WHEN ELITE-TIER
                   MOVE 75.00 TO BASE-PRICE
               WHEN OTHER
                   MOVE 20.00 TO BASE-PRICE
                   DISPLAY "Invalid tier, defaulted to Basic."
           END-EVALUATE.

           IF ADD-SNACKS
               ADD 10.00 TO ADDON-PRICE
           END-IF.

           IF ADD-GEAR
               ADD 25.00 TO ADDON-PRICE
           END-IF.

           IF ELITE-TIER
               MOVE ZERO TO SHIPPING
           END-IF.

           COMPUTE MONTHLY-TOTAL = BASE-PRICE + ADDON-PRICE + SHIPPING.
           COMPUTE ANNUAL-TOTAL = MONTHLY-TOTAL * 12.

       PRINT-SUMMARY.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "      SUBSCRIPTION ENROLLMENT          "
           DISPLAY "======================================="
           DISPLAY "Welcome, " SUB-NAME "!"
           DISPLAY "---------------------------------------"
           MOVE BASE-PRICE TO F-CURR.
           DISPLAY "Monthly Base Box:   " F-CURR.
           IF ADDON-PRICE > 0
               MOVE ADDON-PRICE TO F-CURR
               DISPLAY "Monthly Add-ons:    " F-CURR
           END-IF.
           MOVE SHIPPING TO F-CURR.
           DISPLAY "Shipping Fee:       " F-CURR.
           DISPLAY "---------------------------------------"
           MOVE MONTHLY-TOTAL TO F-CURR.
           DISPLAY "TOTAL MONTHLY CHARGE: " F-CURR.
           MOVE ANNUAL-TOTAL TO F-CURR.
           DISPLAY "EST. ANNUAL COST:     " F-CURR.
           DISPLAY "=======================================".
