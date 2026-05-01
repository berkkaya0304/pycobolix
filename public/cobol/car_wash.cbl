       IDENTIFICATION DIVISION.
       PROGRAM-ID. CAR-WASH.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WASH-ORDER.
          05 LICENSE-PLATE   PIC X(10).
          05 WASH-PACKAGE    PIC 9.
             88 PKG-BASIC    VALUE 1.
             88 PKG-PREMIUM  VALUE 2.
             88 PKG-ULTIMATE VALUE 3.
          05 WAX-OPTION      PIC X.
             88 WANTS-WAX    VALUE 'Y'.
          05 TIP-AMOUNT      PIC 9(2)V99 VALUE ZERO.

       01 FEES.
          05 BASE-FEE        PIC 9(2)V99 VALUE ZERO.
          05 WAX-FEE         PIC 9(2)V99 VALUE ZERO.
          05 SUB-TOTAL       PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-CHARGE    PIC 9(4)V99 VALUE ZERO.

       01 FMT-AMT            PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-APP.
           DISPLAY "--- SPARKLE CAR WASH ---".
           DISPLAY "License Plate: ".
           ACCEPT LICENSE-PLATE.
           DISPLAY "Package (1=Basic $10, 2=Prem $18, 3=Ult $25): "
           ACCEPT WASH-PACKAGE.
           DISPLAY "Add Hand Wax ($15)? (Y/N): ".
           ACCEPT WAX-OPTION.
           DISPLAY "Add Tip Amount for the crew ($): ".
           ACCEPT TIP-AMOUNT.

           PERFORM CALC-FEES.
           PERFORM ISSUE-TICKET.
           STOP RUN.

       CALC-FEES.
           EVALUATE TRUE
               WHEN PKG-BASIC
                   MOVE 10.00 TO BASE-FEE
               WHEN PKG-PREMIUM
                   MOVE 18.00 TO BASE-FEE
               WHEN PKG-ULTIMATE
                   MOVE 25.00 TO BASE-FEE
               WHEN OTHER
                   MOVE 10.00 TO BASE-FEE
                   DISPLAY "Invalid pkg, defaulted to Basic."
           END-EVALUATE.

           IF WANTS-WAX
               MOVE 15.00 TO WAX-FEE
           ELSE
               MOVE ZERO TO WAX-FEE
           END-IF.

           COMPUTE SUB-TOTAL = BASE-FEE + WAX-FEE.
           COMPUTE TOTAL-CHARGE = SUB-TOTAL + TIP-AMOUNT.

       ISSUE-TICKET.
           DISPLAY " "
           DISPLAY "============================================="
           DISPLAY "           WASH TICKET & RECEIPT             "
           DISPLAY "============================================="
           DISPLAY "Vehicle: " LICENSE-PLATE
           DISPLAY "---------------------------------------------"
           MOVE BASE-FEE TO FMT-AMT.
           DISPLAY "Wash Package Fee:    " FMT-AMT.
           IF WAX-FEE > 0
               MOVE WAX-FEE TO FMT-AMT
               DISPLAY "Hand Wax Add-on:     " FMT-AMT
           END-IF.
           DISPLAY "---------------------------------------------"
           MOVE SUB-TOTAL TO FMT-AMT.
           DISPLAY "Subtotal:            " FMT-AMT.
           MOVE TIP-AMOUNT TO FMT-AMT.
           DISPLAY "Crew Tip:            " FMT-AMT.
           DISPLAY "============================================="
           MOVE TOTAL-CHARGE TO FMT-AMT.
           DISPLAY "TOTAL CHARGED:       " FMT-AMT.
           DISPLAY "   Thank you for choosing Sparkle!           "
           DISPLAY "=============================================".
