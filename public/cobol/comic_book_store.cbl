       IDENTIFICATION DIVISION.
       PROGRAM-ID. COMIC-BOOK-STORE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE-CART.
          05 COMIC-QTY       PIC 9(2) VALUE ZERO.
          05 FIGURE-QTY      PIC 9(2) VALUE ZERO.
          05 BOARD-GAME-QTY  PIC 9(2) VALUE ZERO.
          05 SUB-MONTHLY     PIC X.
             88 IS-SUBSCRIBER VALUE 'Y'.

       01 PRICES.
          05 COMIC-PRC       PIC 9(2)V99 VALUE 4.99.
          05 FIGURE-PRC      PIC 9(2)V99 VALUE 24.99.
          05 BOARD-PRC       PIC 9(2)V99 VALUE 49.99.

       01 CALCS.
          05 C-TOT           PIC 9(3)V99 VALUE ZERO.
          05 F-TOT           PIC 9(3)V99 VALUE ZERO.
          05 B-TOT           PIC 9(3)V99 VALUE ZERO.
          05 SUBTOT          PIC 9(4)V99 VALUE ZERO.
          05 DISCOUNT        PIC 9(3)V99 VALUE ZERO.
          05 FINAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       STORE-START.
           DISPLAY "--- GALAXY HEROES COMICS ---".
           DISPLAY "Single Issue Comics QTY ($4.99 ea): ".
           ACCEPT COMIC-QTY.
           DISPLAY "Action Figures QTY ($24.99 ea): ".
           ACCEPT FIGURE-QTY.
           DISPLAY "Board Games QTY ($49.99 ea): ".
           ACCEPT BOARD-GAME-QTY.
           DISPLAY "Pull-List Subscriber (10% Off)? (Y/N): ".
           ACCEPT SUB-MONTHLY.

           COMPUTE C-TOT = COMIC-QTY * COMIC-PRC.
           COMPUTE F-TOT = FIGURE-QTY * FIGURE-PRC.
           COMPUTE B-TOT = BOARD-GAME-QTY * BOARD-PRC.

           COMPUTE SUBTOT = C-TOT + F-TOT + B-TOT.

           IF IS-SUBSCRIBER
               COMPUTE DISCOUNT = SUBTOT * 0.10
           END-IF.

           COMPUTE FINAL-BILL = SUBTOT - DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             STORE TICKET               "
           DISPLAY "========================================"
           IF COMIC-QTY > 0
               MOVE C-TOT TO DISP
               DISPLAY "Comics (" COMIC-QTY "):           " DISP
           END-IF.
           IF FIGURE-QTY > 0
               MOVE F-TOT TO DISP
               DISPLAY "Figures (" FIGURE-QTY "):          " DISP
           END-IF.
           IF BOARD-GAME-QTY > 0
               MOVE B-TOT TO DISP
               DISPLAY "Board Games (" BOARD-GAME-QTY "):      " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUBTOT TO DISP.
           DISPLAY "Subtotal:            " DISP.
           
           IF IS-SUBSCRIBER
               MOVE DISCOUNT TO DISP
               DISPLAY "Subscriber Disc(10%):-" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-BILL TO DISP.
           DISPLAY "TOTAL BALANCE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
