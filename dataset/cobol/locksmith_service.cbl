       IDENTIFICATION DIVISION.
       PROGRAM-ID. LOCKSMITH-SERVICE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SERVICE-CALL.
          05 CLIENT          PIC X(20).
          05 CALL-TYPE       PIC 9.
             88 HOUSE-LOCK   VALUE 1.
             88 AUTO-LOCK    VALUE 2.
             88 SAFE-CRACK   VALUE 3.
          05 KEYS-CUT        PIC 9(2) VALUE ZERO.
          05 AFTER-HOURS     PIC X.
             88 IS-NIGHT     VALUE 'Y'.

       01 FEES.
          05 TRIP-FEE        PIC 9(2)V99 VALUE 45.00.
          05 LABOR-FEE       PIC 9(3)V99 VALUE ZERO.
          05 KEYS-FEE        PIC 9(2)V99 VALUE ZERO.
          05 NIGHT-SURCHG    PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-CHG       PIC 9(3)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-LOCK.
           DISPLAY "--- METRO LOCK & KEY ---".
           DISPLAY "Client: ".
           ACCEPT CLIENT.
           DISPLAY "Service (1=House $60, 2=Auto $80, 3=Safe $150): ".
           ACCEPT CALL-TYPE.
           DISPLAY "Duplicate Keys Cut On-Site ($5 ea): ".
           ACCEPT KEYS-CUT.
           DISPLAY "Is this an After-Hours Emergency (+ $40)? (Y/N): ".
           ACCEPT AFTER-HOURS.

           EVALUATE TRUE
               WHEN HOUSE-LOCK
                   MOVE 60.00 TO LABOR-FEE
               WHEN AUTO-LOCK
                   MOVE 80.00 TO LABOR-FEE
               WHEN SAFE-CRACK
                   MOVE 150.00 TO LABOR-FEE
               WHEN OTHER
                   MOVE 60.00 TO LABOR-FEE
           END-EVALUATE.

           COMPUTE KEYS-FEE = KEYS-CUT * 5.00.

           IF IS-NIGHT
               MOVE 40.00 TO NIGHT-SURCHG
           END-IF.

           COMPUTE TOTAL-CHG = TRIP-FEE + LABOR-FEE + KEYS-FEE 
                             + NIGHT-SURCHG.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            SERVICE INVOICE             "
           DISPLAY "========================================"
           DISPLAY "Client: " CLIENT
           DISPLAY "----------------------------------------"
           MOVE TRIP-FEE TO DISP.
           DISPLAY "Service Call Trip:  " DISP.
           MOVE LABOR-FEE TO DISP.
           DISPLAY "Unlock Labor Rate:  " DISP.
           
           IF KEYS-CUT > 0
               MOVE KEYS-FEE TO DISP
               DISPLAY "Keys Cut (" KEYS-CUT "):       " DISP
           END-IF.
           
           IF IS-NIGHT
               MOVE NIGHT-SURCHG TO DISP
               DISPLAY "After-Hours Fee:    " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-CHG TO DISP.
           DISPLAY "TOTAL BALANCE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
