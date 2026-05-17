       IDENTIFICATION DIVISION.
       PROGRAM-ID. CONCERT-MERCH.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MERCH-ORDER.
          05 FAN-NAME        PIC X(20).
          05 TSHIRT-QTY      PIC 9(2) VALUE ZERO.
          05 POSTER-QTY      PIC 9(2) VALUE ZERO.
          05 RECORD-QTY      PIC 9(2) VALUE ZERO.
          05 SIGNED-ADDON    PIC X.
             88 WANTS-SIGNED VALUE 'Y'.

       01 PRICES.
          05 TSHIRT-PRC      PIC 9(2)V99 VALUE 35.00.
          05 POSTER-PRC      PIC 9(2)V99 VALUE 15.00.
          05 RECORD-PRC      PIC 9(2)V99 VALUE 40.00.
          05 SIGN-FEE        PIC 9(2)V99 VALUE 20.00.
          
          05 TSHIRT-TOT      PIC 9(4)V99 VALUE ZERO.
          05 POSTER-TOT      PIC 9(3)V99 VALUE ZERO.
          05 RECORD-TOT      PIC 9(4)V99 VALUE ZERO.
          05 SUB-TOT         PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-DUE       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-BOOTH.
           DISPLAY "--- STADIUM MERCH BOOTH ---".
           DISPLAY "Fan Name: ".
           ACCEPT FAN-NAME.
           DISPLAY "Tour T-Shirts ($35 ea): ".
           ACCEPT TSHIRT-QTY.
           DISPLAY "Tour Posters ($15 ea): ".
           ACCEPT POSTER-QTY.
           DISPLAY "Vinyl Records ($40 ea): ".
           ACCEPT RECORD-QTY.
           DISPLAY "Add Band VIP Autograph ($20 flat)? (Y/N): ".
           ACCEPT SIGNED-ADDON.

           COMPUTE TSHIRT-TOT = TSHIRT-QTY * TSHIRT-PRC.
           COMPUTE POSTER-TOT = POSTER-QTY * POSTER-PRC.
           COMPUTE RECORD-TOT = RECORD-QTY * RECORD-PRC.

           COMPUTE SUB-TOT = TSHIRT-TOT + POSTER-TOT + RECORD-TOT.

           IF WANTS-SIGNED
               COMPUTE TOTAL-DUE = SUB-TOT + SIGN-FEE
           ELSE
               MOVE SUB-TOT TO TOTAL-DUE
           END-IF.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           MERCHANDISE RECEIPT          "
           DISPLAY "========================================"
           DISPLAY "Fan: " FAN-NAME
           DISPLAY "----------------------------------------"
           IF TSHIRT-QTY > 0
               MOVE TSHIRT-TOT TO DISP
               DISPLAY "T-Shirts (" TSHIRT-QTY "):        " DISP
           END-IF.
           IF POSTER-QTY > 0
               MOVE POSTER-TOT TO DISP
               DISPLAY "Posters (" POSTER-QTY "):         " DISP
           END-IF.
           IF RECORD-QTY > 0
               MOVE RECORD-TOT TO DISP
               DISPLAY "Vinyl Records (" RECORD-QTY "):   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-TOT TO DISP.
           DISPLAY "Subtotal:            " DISP.
           IF WANTS-SIGNED
               MOVE SIGN-FEE TO DISP
               DISPLAY "VIP Autograph Add-On:" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-DUE TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
