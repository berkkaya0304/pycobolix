       IDENTIFICATION DIVISION.
       PROGRAM-ID. MOVIE-THEATER.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TICKET-INFO.
          05 ADULT-TKTS      PIC 9(2).
          05 CHILD-TKTS      PIC 9(2).
          05 SHOW-TYPE       PIC X.
             88 MATINEE      VALUE 'M'.
             88 EVENING      VALUE 'E'.
             88 IMAX-3D      VALUE 'I'.

       01 CONCESSIONS.
          05 POPCORN-QTY     PIC 9(2).
          05 SODA-QTY        PIC 9(2).

       01 PRICING.
          05 ADULT-FR        PIC 9(2)V99.
          05 CHILD-FR        PIC 9(2)V99.
          05 TKT-TOTAL       PIC 9(4)V99 VALUE ZERO.
          05 SNACK-TOTAL     PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(5)V99 VALUE ZERO.

       01 CURR-FMT           PIC $Z,ZZ9.99.
       01 LOOP-CTRL          PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       MAIN-CASHIER.
           DISPLAY "+++ SATELLITE CINEMAS BOX OFFICE +++".
           PERFORM UNTIL LOOP-CTRL = 'N' OR 'n'
               PERFORM GET-ORDER
               PERFORM CALCULATE-COSTS
               PERFORM PRINT-RECEIPT
               DISPLAY "Next customer? (Y/N): "
               ACCEPT LOOP-CTRL
           END-PERFORM.
           STOP RUN.

       GET-ORDER.
           DISPLAY "Show Type (M=Matinee, E=Evening, I=IMAX): ".
           ACCEPT SHOW-TYPE.
           DISPLAY "Number of Adult Tickets: ".
           ACCEPT ADULT-TKTS.
           DISPLAY "Number of Child Tickets: ".
           ACCEPT CHILD-TKTS.
           DISPLAY "Enter Large Popcorns QTY ($8 each): ".
           ACCEPT POPCORN-QTY.
           DISPLAY "Enter Large Sodas QTY ($5 each): ".
           ACCEPT SODA-QTY.

       CALCULATE-COSTS.
           EVALUATE TRUE
               WHEN MATINEE
                   MOVE 10.00 TO ADULT-FR
                   MOVE 7.00 TO CHILD-FR
               WHEN EVENING
                   MOVE 14.00 TO ADULT-FR
                   MOVE 10.00 TO CHILD-FR
               WHEN IMAX-3D
                   MOVE 18.00 TO ADULT-FR
                   MOVE 14.00 TO CHILD-FR
               WHEN OTHER
                   MOVE 14.00 TO ADULT-FR
                   MOVE 10.00 TO CHILD-FR
                   DISPLAY "Defaulted to Evening Pricing."
           END-EVALUATE.

           COMPUTE TKT-TOTAL = (ADULT-TKTS * ADULT-FR) 
                             + (CHILD-TKTS * CHILD-FR).
           COMPUTE SNACK-TOTAL = (POPCORN-QTY * 8.00) 
                               + (SODA-QTY * 5.00).
           COMPUTE GRAND-TOTAL = TKT-TOTAL + SNACK-TOTAL.

       PRINT-RECEIPT.
           DISPLAY " "
           DISPLAY "----------------------------------------"
           DISPLAY "         CINEMA RECEIPT                 "
           DISPLAY "----------------------------------------"
           MOVE TKT-TOTAL TO CURR-FMT
           DISPLAY "Tickets Total:    " CURR-FMT
           MOVE SNACK-TOTAL TO CURR-FMT
           DISPLAY "Concessions:      " CURR-FMT
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOTAL TO CURR-FMT
           DISPLAY "PLEASE PAY:       " CURR-FMT
           DISPLAY "Enjoy the show!"
           DISPLAY "----------------------------------------".
