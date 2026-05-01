       IDENTIFICATION DIVISION.
       PROGRAM-ID. FARMERS-MARKET.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MARKET-BASKET.
          05 APPLES-LBS      PIC 9(2)V9 VALUE ZERO.
          05 CARROTS-BUNCH   PIC 9(2) VALUE ZERO.
          05 HONEY-JARS      PIC 9(2) VALUE ZERO.
          05 CLOTH-BAG       PIC X.
             88 NEEDS-BAG    VALUE 'Y'.

       01 PRICES.
          05 APPLE-P-LB      PIC 9V99 VALUE 2.99.
          05 CARROT-P-B      PIC 9V99 VALUE 3.50.
          05 HONEY-P-J       PIC 9(2)V99 VALUE 12.00.

       01 TOTALS.
          05 APPLES-TOT      PIC 9(3)V99 VALUE ZERO.
          05 CARROTS-TOT     PIC 9(3)V99 VALUE ZERO.
          05 HONEY-TOT       PIC 9(3)V99 VALUE ZERO.
          05 BAG-FEE         PIC 9V99 VALUE ZERO.
          05 FINAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-STAND.
           DISPLAY "--- SUNNY ACRES FARM STAND ---".
           DISPLAY "Apples (lbs) @ $2.99/lb: ".
           ACCEPT APPLES-LBS.
           DISPLAY "Carrot Bunches @ $3.50 ea: ".
           ACCEPT CARROTS-BUNCH.
           DISPLAY "Local Honey Jars @ $12.00 ea: ".
           ACCEPT HONEY-JARS.
           DISPLAY "Need a reusable cloth bag ($1.50)? (Y/N): ".
           ACCEPT CLOTH-BAG.

           COMPUTE APPLES-TOT = APPLES-LBS * APPLE-P-LB.
           COMPUTE CARROTS-TOT = CARROTS-BUNCH * CARROT-P-B.
           COMPUTE HONEY-TOT = HONEY-JARS * HONEY-P-J.

           IF NEEDS-BAG
               MOVE 1.50 TO BAG-FEE
           END-IF.

           COMPUTE FINAL-BILL = APPLES-TOT + CARROTS-TOT 
                              + HONEY-TOT + BAG-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "        FARMERS MARKET RECIEPT          "
           DISPLAY "========================================"
           IF APPLES-LBS > 0
               MOVE APPLES-TOT TO DISP
               DISPLAY "Gala Apples (" APPLES-LBS " lbs): " DISP
           END-IF.
           IF CARROTS-BUNCH > 0
               MOVE CARROTS-TOT TO DISP
               DISPLAY "Carrots (" CARROTS-BUNCH " bch):     " DISP
           END-IF.
           IF HONEY-JARS > 0
               MOVE HONEY-TOT TO DISP
               DISPLAY "Local Honey (" HONEY-JARS " jar):  " DISP
           END-IF.
           IF NEEDS-BAG
               DISPLAY "Reusable Bag:           $    1.50"
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-BILL TO DISP.
           DISPLAY "TOTAL PRODUCE TOTAL:" DISP.
           DISPLAY "========================================".
           STOP RUN.
