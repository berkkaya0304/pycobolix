       IDENTIFICATION DIVISION.
       PROGRAM-ID. HOTEL-CHECKOUT.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 GUEST-INFO.
          05 ROOM-NUMBER     PIC 9(4).
          05 GUEST-NAME      PIC X(25).

       01 STAY-CHARGES.
          05 OUTSTANDING-BAL PIC 9(5)V99.
          05 MINIBAR-USE     PIC X.
             88 USED-MINIBAR VALUE 'Y'.
          05 MINIBAR-FEE     PIC 9(3)V99 VALUE ZERO.
          05 ROOM-SERVICE    PIC 9(3)V99 VALUE ZERO.
          05 ROOM-DAMAGES    PIC 9(4)V99 VALUE ZERO.
          
       01 FINAL-CALCS.
          05 SUB-TOT         PIC 9(6)V99.
          05 RESORT-FEE      PIC 9(3)V99 VALUE 25.00.
          05 TAX             PIC 9(5)V99.
          05 FINAL-BILL      PIC 9(7)V99.

       01 DISP-FMT           PIC $ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- PARADISE INN CHECKOUT ---".
           DISPLAY "Room Number: ".
           ACCEPT ROOM-NUMBER.
           DISPLAY "Guest Name: ".
           ACCEPT GUEST-NAME.
           DISPLAY "Oustanding Room Balance ($): ".
           ACCEPT OUTSTANDING-BAL.
           
           DISPLAY "Minibar used? (Y/N): ".
           ACCEPT MINIBAR-USE.
           IF USED-MINIBAR
               DISPLAY "Total Minibar Charge ($): "
               ACCEPT MINIBAR-FEE
           END-IF.

           DISPLAY "Total Room Service Charges ($): ".
           ACCEPT ROOM-SERVICE.
           DISPLAY "Room Damages Assessed ($): ".
           ACCEPT ROOM-DAMAGES.

           PERFORM CALC-BILL.
           PERFORM ISSUE-RECEIPT.
           STOP RUN.

       CALC-BILL.
           COMPUTE SUB-TOT = OUTSTANDING-BAL + MINIBAR-FEE 
                           + ROOM-SERVICE + ROOM-DAMAGES + RESORT-FEE.
                           
           COMPUTE TAX = SUB-TOT * 0.11.
           COMPUTE FINAL-BILL = SUB-TOT + TAX.

       ISSUE-RECEIPT.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "           FINAL GUEST INVOICE           "
           DISPLAY "========================================="
           DISPLAY "Room: " ROOM-NUMBER "    Guest: " GUEST-NAME
           DISPLAY "-----------------------------------------"
           MOVE OUTSTANDING-BAL TO DISP-FMT.
           DISPLAY "Room Stay Balance: " DISP-FMT.
           MOVE RESORT-FEE TO DISP-FMT.
           DISPLAY "Daily Resort Fee:  " DISP-FMT.
           
           IF MINIBAR-FEE > 0
               MOVE MINIBAR-FEE TO DISP-FMT
               DISPLAY "Minibar Charges:   " DISP-FMT
           END-IF.
           
           IF ROOM-SERVICE > 0
               MOVE ROOM-SERVICE TO DISP-FMT
               DISPLAY "Room Service:      " DISP-FMT
           END-IF.
           
           IF ROOM-DAMAGES > 0
               MOVE ROOM-DAMAGES TO DISP-FMT
               DISPLAY "Damage Assessment: " DISP-FMT
           END-IF.
           DISPLAY "-----------------------------------------"
           MOVE SUB-TOT TO DISP-FMT.
           DISPLAY "Sub Total:         " DISP-FMT.
           MOVE TAX TO DISP-FMT.
           DISPLAY "Taxes (11%):       " DISP-FMT.
           DISPLAY "-----------------------------------------"
           MOVE FINAL-BILL TO DISP-FMT.
           DISPLAY "FINAL AMOUNT SETTLED:" DISP-FMT.
           DISPLAY "=========================================".
