       IDENTIFICATION DIVISION.
       PROGRAM-ID. ART-GALLERY.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE-APP.
          05 COLLECTOR-NAME  PIC X(20).
          05 ART-TITLE       PIC X(25).
          05 ART-PRICE       PIC 9(6)V99.
          05 SHIP-METHOD     PIC 9.
             88 PICKUP       VALUE 1.
             88 DOMESTIC     VALUE 2.
             88 INT-SHIP     VALUE 3.

       01 FEES.
          05 SHIP-FEE        PIC 9(4)V99 VALUE ZERO.
          05 HANDLING-FEE    PIC 9(3)V99 VALUE ZERO.
          05 GRAND-APP       PIC 9(7)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-SALE.
           DISPLAY "--- MODERN CANVAS GALLERY ---".
           DISPLAY "Collector Name: ".
           ACCEPT COLLECTOR-NAME.
           DISPLAY "Artwork Title: ".
           ACCEPT ART-TITLE.
           DISPLAY "Artwork Price ($): ".
           ACCEPT ART-PRICE.
           DISPLAY "Delivery: 1=Pickup, 2=Domestic, 3=Intl: ".
           ACCEPT SHIP-METHOD.

           EVALUATE TRUE
               WHEN PICKUP
                   MOVE ZERO TO SHIP-FEE
                   MOVE ZERO TO HANDLING-FEE
               WHEN DOMESTIC
                   COMPUTE SHIP-FEE = ART-PRICE * 0.03
                   MOVE 50.00 TO HANDLING-FEE
               WHEN INT-SHIP
                   COMPUTE SHIP-FEE = ART-PRICE * 0.08
                   MOVE 150.00 TO HANDLING-FEE
               WHEN OTHER
                   MOVE ZERO TO SHIP-FEE
           END-EVALUATE.

           COMPUTE GRAND-APP = ART-PRICE + SHIP-FEE + HANDLING-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           GALLERY INVOICE              "
           DISPLAY "========================================"
           DISPLAY "Aquired By: " COLLECTOR-NAME
           DISPLAY "Artwork:    " ART-TITLE
           DISPLAY "----------------------------------------"
           MOVE ART-PRICE TO DISP.
           DISPLAY "Base Price:          " DISP.
           
           IF SHIP-FEE > 0
               MOVE SHIP-FEE TO DISP
               DISPLAY "Freight Assessed:    " DISP
           END-IF.
           
           IF HANDLING-FEE > 0
               MOVE HANDLING-FEE TO DISP
               DISPLAY "Crate/Handling:      " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-APP TO DISP.
           DISPLAY "TOTAL PAYABLE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
