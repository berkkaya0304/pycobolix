       IDENTIFICATION DIVISION.
       PROGRAM-ID. LAUNDRY-SERVICE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CUSTOMER-INFO.
          05 CUST-NAME       PIC X(25).
          05 PHONE-NUM       PIC X(10).
          
       01 ORDER-ITEMS.
          05 SHIRTS-QTY      PIC 9(2).
          05 PANTS-QTY       PIC 9(2).
          05 SUITS-QTY       PIC 9(2).
          
       01 OPTIONS.
          05 RUSH-SERVICE    PIC X.
             88 IS-RUSH      VALUE 'Y'.

       01 PRICING-CALCS.
          05 SHIRT-COST      PIC 9(3)V99 VALUE ZERO.
          05 PANT-COST       PIC 9(3)V99 VALUE ZERO.
          05 SUIT-COST       PIC 9(3)V99 VALUE ZERO.
          05 RUSH-FEE        PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP-FMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-APP.
           DISPLAY "=== FRESH & CLEAN DRY CLEANERS ===".
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Phone Number: ".
           ACCEPT PHONE-NUM.

           DISPLAY "Number of Shirts ($4.50 ea): ".
           ACCEPT SHIRTS-QTY.
           DISPLAY "Number of Pants ($6.00 ea): ".
           ACCEPT PANTS-QTY.
           DISPLAY "Number of Suits ($15.00 ea): ".
           ACCEPT SUITS-QTY.
           DISPLAY "Rush 24-hour service? (+$10 flat) (Y/N): ".
           ACCEPT RUSH-SERVICE.

           PERFORM CALC-BILL.
           PERFORM PRINT-TICKET.
           STOP RUN.

       CALC-BILL.
           COMPUTE SHIRT-COST = SHIRTS-QTY * 4.50.
           COMPUTE PANT-COST = PANTS-QTY * 6.00.
           COMPUTE SUIT-COST = SUITS-QTY * 15.00.
           
           COMPUTE TOTAL-BILL = SHIRT-COST + PANT-COST + SUIT-COST.

           IF IS-RUSH
               MOVE 10.00 TO RUSH-FEE
               ADD RUSH-FEE TO TOTAL-BILL
           END-IF.

       PRINT-TICKET.
           DISPLAY " "
           DISPLAY "-----------------------------------------"
           DISPLAY "          LAUNDRY CLAIM TICKET           "
           DISPLAY "-----------------------------------------"
           DISPLAY "Name: " CUST-NAME " | Ph: " PHONE-NUM
           DISPLAY "-----------------------------------------"
           IF SHIRTS-QTY > 0
               MOVE SHIRT-COST TO DISP-FMT
               DISPLAY SHIRTS-QTY " x Shirts:       " DISP-FMT
           END-IF
           IF PANTS-QTY > 0
               MOVE PANT-COST TO DISP-FMT
               DISPLAY PANTS-QTY " x Pants:        " DISP-FMT
           END-IF
           IF SUITS-QTY > 0
               MOVE SUIT-COST TO DISP-FMT
               DISPLAY SUITS-QTY " x Suits:        " DISP-FMT
           END-IF
           DISPLAY "-----------------------------------------"
           IF RUSH-FEE > 0
               MOVE RUSH-FEE TO DISP-FMT
               DISPLAY "Rush Service Fee: " DISP-FMT
           END-IF
           MOVE TOTAL-BILL TO DISP-FMT.
           DISPLAY "GRAND TOTAL:      " DISP-FMT.
           DISPLAY "-----------------------------------------".
