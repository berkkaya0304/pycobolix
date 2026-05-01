       IDENTIFICATION DIVISION.
       PROGRAM-ID. WATCH-REPAIR.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 REPAIR-ORDER.
          05 CLIENT-NAME     PIC X(20).
          05 WATCH-BRAND     PIC X(15).
          05 SV-BATTERY      PIC X.
             88 FIX-BATT     VALUE 'Y'.
          05 SV-STRAP        PIC X.
             88 FIX-STRAP    VALUE 'Y'.
          05 SV-POLISH       PIC X.
             88 FIX-POLISH   VALUE 'Y'.
          05 LUXURY-TIER     PIC X.
             88 IS-LUXURY    VALUE 'Y'.

       01 FEES.
          05 BATT-FEE        PIC 9(2)V99 VALUE ZERO.
          05 STRAP-FEE       PIC 9(2)V99 VALUE ZERO.
          05 POLISH-FEE      PIC 9(2)V99 VALUE ZERO.
          05 SUB-TOT         PIC 9(4)V99 VALUE ZERO.
          05 LUXURY-SURCHG   PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-FIX.
           DISPLAY "--- TIC-TOCK WATCH REPAIR ---".
           DISPLAY "Client: ".
           ACCEPT CLIENT-NAME.
           DISPLAY "Watch Brand: ".
           ACCEPT WATCH-BRAND.
           DISPLAY "Is this a luxury timepiece (+25%)? (Y/N): ".
           ACCEPT LUXURY-TIER.
           DISPLAY "Replace Battery ($20)? (Y/N): ".
           ACCEPT SV-BATTERY.
           DISPLAY "Replace/Fix Strap ($35)? (Y/N): ".
           ACCEPT SV-STRAP.
           DISPLAY "Surface Polish ($45)? (Y/N): ".
           ACCEPT SV-POLISH.

           IF FIX-BATT
               MOVE 20.00 TO BATT-FEE
           END-IF.
           IF FIX-STRAP
               MOVE 35.00 TO STRAP-FEE
           END-IF.
           IF FIX-POLISH
               MOVE 45.00 TO POLISH-FEE
           END-IF.

           COMPUTE SUB-TOT = BATT-FEE + STRAP-FEE + POLISH-FEE.

           IF IS-LUXURY
               COMPUTE LUXURY-SURCHG = SUB-TOT * 0.25
           END-IF.

           COMPUTE GRAND-TOT = SUB-TOT + LUXURY-SURCHG.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            SERVICE TICKET              "
           DISPLAY "========================================"
           DISPLAY "Client: " CLIENT-NAME
           DISPLAY "Brand:  " WATCH-BRAND
           DISPLAY "----------------------------------------"
           IF FIX-BATT
               MOVE BATT-FEE TO DISP
               DISPLAY "Battery Service:    " DISP
           END-IF.
           IF FIX-STRAP
               MOVE STRAP-FEE TO DISP
               DISPLAY "Strap Replacement:  " DISP
           END-IF.
           IF FIX-POLISH
               MOVE POLISH-FEE TO DISP
               DISPLAY "Polishing Service:  " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           IF IS-LUXURY
               MOVE LUXURY-SURCHG TO DISP
               DISPLAY "Luxury Brand Fee:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL SERVICE COST: " DISP.
           DISPLAY "========================================".
           STOP RUN.
