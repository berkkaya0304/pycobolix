       IDENTIFICATION DIVISION.
       PROGRAM-ID. FURNITURE-STORE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE.
          05 BUYER-NAME      PIC X(20).
          05 SOFA-QTY        PIC 9(2) VALUE ZERO.
          05 TABLE-QTY       PIC 9(2) VALUE ZERO.
          05 CHAIR-QTY       PIC 9(2) VALUE ZERO.
          05 HOME-DELIVERY   PIC X.
             88 WANTS-DELIV  VALUE 'Y'.

       01 PRICES.
          05 SOFA-PRC        PIC 9(3)V99 VALUE 599.00.
          05 TABLE-PRC       PIC 9(3)V99 VALUE 349.00.
          05 CHAIR-PRC       PIC 9(2)V99 VALUE 85.00.
          05 DELIV-FEE       PIC 9(2)V99 VALUE ZERO.

       01 TOTS.
          05 S-TOT           PIC 9(4)V99 VALUE ZERO.
          05 T-TOT           PIC 9(4)V99 VALUE ZERO.
          05 C-TOT           PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       HOME-START.
           DISPLAY "--- COZY LIVING FURNITURE ---".
           DISPLAY "Customer: ".
           ACCEPT BUYER-NAME.
           DISPLAY "Sectional Sofas ($599.00 ea): ".
           ACCEPT SOFA-QTY.
           DISPLAY "Dining Tables ($349.00 ea): ".
           ACCEPT TABLE-QTY.
           DISPLAY "Dining Chairs ($85.00 ea): ".
           ACCEPT CHAIR-QTY.
           DISPLAY "White-Glove Delivery ($99 flat)? (Y/N): ".
           ACCEPT HOME-DELIVERY.

           COMPUTE S-TOT = SOFA-QTY * SOFA-PRC.
           COMPUTE T-TOT = TABLE-QTY * TABLE-PRC.
           COMPUTE C-TOT = CHAIR-QTY * CHAIR-PRC.

           IF WANTS-DELIV
               MOVE 99.00 TO DELIV-FEE
           END-IF.

           COMPUTE GRAND-TOT = S-TOT + T-TOT + C-TOT + DELIV-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             STORE RECEIPT              "
           DISPLAY "========================================"
           DISPLAY "Customer: " BUYER-NAME
           DISPLAY "----------------------------------------"
           IF SOFA-QTY > 0
               MOVE S-TOT TO DISP
               DISPLAY "Sofas (" SOFA-QTY "):           " DISP
           END-IF.
           IF TABLE-QTY > 0
               MOVE T-TOT TO DISP
               DISPLAY "Tables (" TABLE-QTY "):          " DISP
           END-IF.
           IF CHAIR-QTY > 0
               MOVE C-TOT TO DISP
               DISPLAY "Chairs (" CHAIR-QTY "):          " DISP
           END-IF.
           IF WANTS-DELIV
               MOVE DELIV-FEE TO DISP
               DISPLAY "Delivery Fee:       " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL ORDER:        " DISP.
           DISPLAY "========================================".
           STOP RUN.
