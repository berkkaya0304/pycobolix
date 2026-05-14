       IDENTIFICATION DIVISION.
       PROGRAM-ID. BOXING-GYM.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 GYM-VISIT.
          05 FIGHTER-NAME    PIC X(20).
          05 SESSION-TYPE    PIC 9.
             88 OPEN-GYM     VALUE 1.
             88 GROUP-CLASS  VALUE 2.
             88 PRIV-COACH   VALUE 3.
          05 RENT-GLOVES     PIC X.
             88 WANTS-GLOVES VALUE 'Y'.
          05 RENT-WRAPS      PIC X.
             88 WANTS-WRAPS  VALUE 'Y'.

       01 FEES.
          05 ENTRY-FEE       PIC 9(3)V99 VALUE ZERO.
          05 GLOVE-FEE       PIC 9(2)V99 VALUE ZERO.
          05 WRAP-FEE        PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-DUE       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- IRON FIST BOXING GYM ---".
           DISPLAY "Fighter: ".
           ACCEPT FIGHTER-NAME.
           DISPLAY "Entry (1=Open Gym $15, 2=Class $25, 3=Coach $80): ".
           ACCEPT SESSION-TYPE.
           DISPLAY "Rent Sparring Gloves ($5)? (Y/N): ".
           ACCEPT RENT-GLOVES.
           DISPLAY "Buy Hand Wraps ($8)? (Y/N): ".
           ACCEPT RENT-WRAPS.

           EVALUATE TRUE
               WHEN OPEN-GYM
                   MOVE 15.00 TO ENTRY-FEE
               WHEN GROUP-CLASS
                   MOVE 25.00 TO ENTRY-FEE
               WHEN PRIV-COACH
                   MOVE 80.00 TO ENTRY-FEE
               WHEN OTHER
                   MOVE 15.00 TO ENTRY-FEE
           END-EVALUATE.

           IF WANTS-GLOVES
               MOVE 5.00 TO GLOVE-FEE
           END-IF.

           IF WANTS-WRAPS
               MOVE 8.00 TO WRAP-FEE
           END-IF.

           COMPUTE TOTAL-DUE = ENTRY-FEE + GLOVE-FEE + WRAP-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             GYM CHECK-IN               "
           DISPLAY "========================================"
           DISPLAY "Name: " FIGHTER-NAME
           DISPLAY "----------------------------------------"
           MOVE ENTRY-FEE TO DISP.
           DISPLAY "Session Access:      " DISP.
           
           IF WANTS-GLOVES
               MOVE GLOVE-FEE TO DISP
               DISPLAY "Glove Rental:        " DISP
           END-IF.
           
           IF WANTS-WRAPS
               MOVE WRAP-FEE TO DISP
               DISPLAY "Hand Wraps Purchase: " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-DUE TO DISP.
           DISPLAY "TOTAL BALANCE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
