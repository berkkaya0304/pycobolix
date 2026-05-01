       IDENTIFICATION DIVISION.
       PROGRAM-ID. GYM-CLASS.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MEMBER-INFO.
          05 MEMBER-NAME     PIC X(20).
          05 CLASS-SELECTION PIC 9.
             88 CLS-YOGA     VALUE 1.
             88 CLS-SPIN     VALUE 2.
             88 CLS-PILATES  VALUE 3.
          05 GUEST-PASSES    PIC 9(2) VALUE ZERO.
          05 TOWEL-RENTAL    PIC X.
             88 WANTS-TOWEL  VALUE 'Y'.

       01 FEES.
          05 CLASS-FEE       PIC 9(2)V99 VALUE ZERO.
          05 GUEST-FEE       PIC 9(3)V99 VALUE ZERO.
          05 TOWEL-FEE       PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-CHG       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-BOOKING.
           DISPLAY "--- FIT-LIFE CLASS BOOKING ---".
           DISPLAY "Member Name: ".
           ACCEPT MEMBER-NAME.
           DISPLAY "Class (1=Yoga $15, 2=Spin $20, 3=Pilates $25): ".
           ACCEPT CLASS-SELECTION.
           DISPLAY "Number of Non-Member Guests ($10 ea): ".
           ACCEPT GUEST-PASSES.
           DISPLAY "Rent Premium Towel Service ($3)? (Y/N): ".
           ACCEPT TOWEL-RENTAL.

           EVALUATE TRUE
               WHEN CLS-YOGA
                   MOVE 15.00 TO CLASS-FEE
               WHEN CLS-SPIN
                   MOVE 20.00 TO CLASS-FEE
               WHEN CLS-PILATES
                   MOVE 25.00 TO CLASS-FEE
               WHEN OTHER
                   MOVE 15.00 TO CLASS-FEE
           END-EVALUATE.

           COMPUTE GUEST-FEE = GUEST-PASSES * 10.00.

           IF WANTS-TOWEL
               MOVE 3.00 TO TOWEL-FEE
           END-IF.

           COMPUTE TOTAL-CHG = CLASS-FEE + GUEST-FEE + TOWEL-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           CLASS RESERVATION            "
           DISPLAY "========================================"
           DISPLAY "Member: " MEMBER-NAME
           DISPLAY "----------------------------------------"
           MOVE CLASS-FEE TO DISP.
           DISPLAY "Class Base Fee:       " DISP.
           
           IF GUEST-PASSES > 0
               MOVE GUEST-FEE TO DISP
               DISPLAY "Guest Passes (" GUEST-PASSES "):      " DISP
           END-IF.
           
           IF WANTS-TOWEL
               MOVE TOWEL-FEE TO DISP
               DISPLAY "Towel Service Option: " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-CHG TO DISP.
           DISPLAY "TOTAL CHARGED:        " DISP.
           DISPLAY "========================================".
           STOP RUN.
