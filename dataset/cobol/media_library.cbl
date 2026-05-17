       IDENTIFICATION DIVISION.
       PROGRAM-ID. MEDIA-LIBRARY.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RETURN-INFO.
          05 MEMBER-ID       PIC X(8).
          05 ITEM-TYPE       PIC 9.
             88 IS-BOOK      VALUE 1.
             88 IS-DVD       VALUE 2.
             88 IS-LAPTOP    VALUE 3.
          05 DAYS-OVERDUE    PIC 9(3).

       01 FEES.
          05 RATE-PER-DAY    PIC 9(2)V99 VALUE ZERO.
          05 MAX-FINE        PIC 9(3)V99 VALUE ZERO.
          05 CALC-FINE       PIC 9(4)V99 VALUE ZERO.
          05 PROCESS-FEE     PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP-MONEY         PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-LIB.
           DISPLAY "--- CITY LIBRARY RETURNS ---".
           DISPLAY "Member ID: ".
           ACCEPT MEMBER-ID.
           DISPLAY "Item Type (1=Book, 2=DVD, 3=Laptop): ".
           ACCEPT ITEM-TYPE.
           DISPLAY "Days Overdue: ".
           ACCEPT DAYS-OVERDUE.

           PERFORM CALCULATE-FINE.
           PERFORM PRINT-NOTICE.
           STOP RUN.

       CALCULATE-FINE.
           EVALUATE TRUE
               WHEN IS-BOOK
                   MOVE 0.25 TO RATE-PER-DAY
                   MOVE 10.00 TO MAX-FINE
               WHEN IS-DVD
                   MOVE 1.50 TO RATE-PER-DAY
                   MOVE 30.00 TO MAX-FINE
               WHEN IS-LAPTOP
                   MOVE 20.00 TO RATE-PER-DAY
                   MOVE 500.00 TO MAX-FINE
                   MOVE 15.00 TO PROCESS-FEE
               WHEN OTHER
                   MOVE 0.25 TO RATE-PER-DAY
                   MOVE 10.00 TO MAX-FINE
           END-EVALUATE.

           COMPUTE CALC-FINE = DAYS-OVERDUE * RATE-PER-DAY.
           
           IF CALC-FINE > MAX-FINE
               MOVE MAX-FINE TO CALC-FINE
               DISPLAY ">>> Fine capped at Maximum Amount."
           END-IF.

           COMPUTE TOTAL-BILL = CALC-FINE + PROCESS-FEE.

       PRINT-NOTICE.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          LIBRARY FINE NOTICE           "
           DISPLAY "========================================"
           DISPLAY "Member: " MEMBER-ID
           DISPLAY "Days Late: " DAYS-OVERDUE
           DISPLAY "----------------------------------------"
           
           IF DAYS-OVERDUE = 0
               DISPLAY "Item returned on time. No fines."
           ELSE
               MOVE CALC-FINE TO DISP-MONEY
               DISPLAY "Late Fine:         " DISP-MONEY
               IF PROCESS-FEE > 0
                   MOVE PROCESS-FEE TO DISP-MONEY
                   DISPLAY "Processing Fee:    " DISP-MONEY
               END-IF
               DISPLAY "----------------------------------------"
               MOVE TOTAL-BILL TO DISP-MONEY
               DISPLAY "TOTAL DUE:         " DISP-MONEY
           END-IF.
           DISPLAY "========================================".
