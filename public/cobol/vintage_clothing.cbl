       IDENTIFICATION DIVISION.
       PROGRAM-ID. VINTAGE-CLOTHING.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE.
          05 SHIRT-QTY       PIC 9(2) VALUE ZERO.
          05 JACKET-QTY      PIC 9(2) VALUE ZERO.
          05 PANTS-QTY       PIC 9(2) VALUE ZERO.
          05 DONATION        PIC X.
             88 WANTS-DONATE VALUE 'Y'.

       01 PRICING.
          05 SHIRT-PRC       PIC 9(2)V99 VALUE 15.00.
          05 JACKET-PRC      PIC 9(2)V99 VALUE 45.00.
          05 PANT-PRC        PIC 9(2)V99 VALUE 20.00.

       01 STATS.
          05 SUB-TOT         PIC 9(4)V99 VALUE ZERO.
          05 DISCOUNT        PIC 9(3)V99 VALUE ZERO.
          05 FINAL-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       THRIFT-START.
           DISPLAY "--- SECOND CHANCE THRIFT & VINTAGE ---".
           DISPLAY "Graphic T-Shirts ($15.00 ea): ".
           ACCEPT SHIRT-QTY.
           DISPLAY "Leather/Denim Jackets ($45.00 ea): ".
           ACCEPT JACKET-QTY.
           DISPLAY "Vintage Pants/Jeans ($20.00 ea): ".
           ACCEPT PANTS-QTY.
           DISPLAY "Donate $2 to Charity? (Y/N): ".
           ACCEPT DONATION.

           COMPUTE SUB-TOT = (SHIRT-QTY * SHIRT-PRC)
                           + (JACKET-QTY * JACKET-PRC)
                           + (PANTS-QTY * PANT-PRC).

           IF SUB-TOT > 100.00
               COMPUTE DISCOUNT = SUB-TOT * 0.15
           END-IF.

           COMPUTE FINAL-TOT = SUB-TOT - DISCOUNT.

           IF WANTS-DONATE
               ADD 2.00 TO FINAL-TOT
           END-IF.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          SHOPPING RECEIPT              "
           DISPLAY "========================================"
           IF SHIRT-QTY > 0
               COMPUTE DISP = SHIRT-QTY * SHIRT-PRC
               DISPLAY SHIRT-QTY "x T-Shirts:         " DISP
           END-IF.
           IF JACKET-QTY > 0
               COMPUTE DISP = JACKET-QTY * JACKET-PRC
               DISPLAY JACKET-QTY "x Jackets:          " DISP
           END-IF.
           IF PANTS-QTY > 0
               COMPUTE DISP = PANTS-QTY * PANT-PRC
               DISPLAY PANTS-QTY "x Pants:            " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-TOT TO DISP.
           DISPLAY "Cart Subtotal:      " DISP.
           
           IF DISCOUNT > 0
               MOVE DISCOUNT TO DISP
               DISPLAY "Bulk Discount 15%: -" DISP
           END-IF.
           
           IF WANTS-DONATE
               DISPLAY "Charity Donation:    $    2.00"
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-TOT TO DISP.
           DISPLAY "GRAND TOTAL:        " DISP.
           DISPLAY "========================================".
           STOP RUN.
