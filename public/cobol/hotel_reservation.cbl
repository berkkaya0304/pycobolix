       IDENTIFICATION DIVISION.
       PROGRAM-ID. HOTEL-RESERVATION.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 GUEST-INFO.
          05 GUEST-NAME      PIC X(30).
          05 ROOM-TYPE       PIC X.
             88 RM-STANDARD  VALUE 'S'.
             88 RM-DELUXE    VALUE 'D'.
             88 RM-SUITE     VALUE 'P'.
          05 NIGHTS          PIC 9(2).
          
       01 COST-PER-NIGHT     PIC 9(4)V99.
       01 ROOM-TOTAL         PIC 9(6)V99.
       
       01 ADDONS.
          05 BREAKFAST-INC   PIC X.
             88 HAS-BRKFST   VALUE 'Y'.
          05 SPA-ACCESS      PIC X.
             88 HAS-SPA      VALUE 'Y'.
          05 ADDON-TOTAL     PIC 9(4)V99 VALUE ZERO.
          
       01 GRAND-BILL         PIC 9(6)V99.
       01 DISP-BILL          PIC $ZZZ,ZZ9.99.
       
       01 CONTINUE-PROG      PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       BEGIN.
           DISPLAY "--- HOTEL BOOKING SYSTEM ---".
           PERFORM UNTIL CONTINUE-PROG = 'N' OR 'n'
               PERFORM GET-BOOKING
               PERFORM CALC-BILL
               PERFORM SHOW-RECEIPT
               DISPLAY "Process another guest? (Y/N): "
               ACCEPT CONTINUE-PROG
           END-PERFORM.
           DISPLAY "System Shutdown.".
           STOP RUN.

       GET-BOOKING.
           DISPLAY "Enter Guest Name: ".
           ACCEPT GUEST-NAME.
           DISPLAY "Select Room Type (S=Std, D=Deluxe, P=Suite): ".
           ACCEPT ROOM-TYPE.
           DISPLAY "Number of Nights: ".
           ACCEPT NIGHTS.
           DISPLAY "Include Breakfast? ($20/night) (Y/N): ".
           ACCEPT BREAKFAST-INC.
           DISPLAY "Include Spa Access? ($50 flat fee) (Y/N): ".
           ACCEPT SPA-ACCESS.

       CALC-BILL.
           EVALUATE TRUE
               WHEN RM-STANDARD
                   MOVE 100.00 TO COST-PER-NIGHT
               WHEN RM-DELUXE
                   MOVE 180.00 TO COST-PER-NIGHT
               WHEN RM-SUITE
                   MOVE 350.00 TO COST-PER-NIGHT
               WHEN OTHER
                   MOVE 100.00 TO COST-PER-NIGHT
                   DISPLAY "Invalid room type, defaulted to Standard."
           END-EVALUATE.

           COMPUTE ROOM-TOTAL = COST-PER-NIGHT * NIGHTS.
           MOVE ZERO TO ADDON-TOTAL.
           
           IF HAS-BRKFST
               COMPUTE ADDON-TOTAL = ADDON-TOTAL + (20.00 * NIGHTS)
           END-IF.
           
           IF HAS-SPA
               COMPUTE ADDON-TOTAL = ADDON-TOTAL + 50.00
           END-IF.
           
           COMPUTE GRAND-BILL = ROOM-TOTAL + ADDON-TOTAL.

       SHOW-RECEIPT.
           DISPLAY " ".
           DISPLAY "***********************************".
           DISPLAY "       GUEST RECEIPT               ".
           DISPLAY "***********************************".
           DISPLAY "Guest: " GUEST-NAME.
           DISPLAY "Nights: " NIGHTS.
           MOVE ROOM-TOTAL TO DISP-BILL.
           DISPLAY "Room Charge:    " DISP-BILL.
           MOVE ADDON-TOTAL TO DISP-BILL.
           DISPLAY "Add-Ons Charge: " DISP-BILL.
           DISPLAY "-----------------------------------".
           MOVE GRAND-BILL TO DISP-BILL.
           DISPLAY "TOTAL BILL:     " DISP-BILL.
           DISPLAY "***********************************".
           DISPLAY " ".
