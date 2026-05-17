       IDENTIFICATION DIVISION.
       PROGRAM-ID. MINI-GOLF.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PLAYERS.
          05 ADULT-QTY       PIC 9(2).
          05 CHILD-QTY       PIC 9(2).
          05 COURSE-TYPE     PIC 9.
             88 HALF-COURSE  VALUE 1.
             88 FULL-COURSE  VALUE 2.

       01 RATES.
          05 ADULT-RATE      PIC 9(2)V99 VALUE ZERO.
          05 CHILD-RATE      PIC 9(2)V99 VALUE ZERO.
          05 ADULT-TOT       PIC 9(3)V99 VALUE ZERO.
          05 CHILD-TOT       PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-GAME.
           DISPLAY "--- GATOR GOLF ADVENTURE ---".
           DISPLAY "Number of Adults: ".
           ACCEPT ADULT-QTY.
           DISPLAY "Number of Children (Under 12): ".
           ACCEPT CHILD-QTY.
           DISPLAY "Course (1=9 Holes, 2=18 Holes): ".
           ACCEPT COURSE-TYPE.

           EVALUATE TRUE
               WHEN HALF-COURSE
                   MOVE 12.00 TO ADULT-RATE
                   MOVE 8.00 TO CHILD-RATE
               WHEN FULL-COURSE
                   MOVE 18.00 TO ADULT-RATE
                   MOVE 12.00 TO CHILD-RATE
               WHEN OTHER
                   MOVE 12.00 TO ADULT-RATE
                   MOVE 8.00 TO CHILD-RATE
           END-EVALUATE.

           COMPUTE ADULT-TOT = ADULT-QTY * ADULT-RATE.
           COMPUTE CHILD-TOT = CHILD-QTY * CHILD-RATE.
           
           COMPUTE GRAND-TOT = ADULT-TOT + CHILD-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           MINI GOLF RECEIPT            "
           DISPLAY "========================================"
           IF FULL-COURSE
               DISPLAY "Course Selected: 18-Hole Adventure"
           ELSE
               DISPLAY "Course Selected: 9-Hole Quick Run"
           END-IF
           DISPLAY "----------------------------------------"
           IF ADULT-QTY > 0
               MOVE ADULT-TOT TO DISP
               DISPLAY ADULT-QTY "x Adult Tickets:   " DISP
           END-IF.
           IF CHILD-QTY > 0
               MOVE CHILD-TOT TO DISP
               DISPLAY CHILD-QTY "x Child Tickets:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:  " DISP.
           DISPLAY "========================================".
           STOP RUN.
