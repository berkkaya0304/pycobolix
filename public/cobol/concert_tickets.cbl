       IDENTIFICATION DIVISION.
       PROGRAM-ID. CONCERT-TICKETS.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE-DATA.
          05 BUYER-NAME      PIC X(25).
          05 GEN-ADM-QTY     PIC 9(2) VALUE ZERO.
          05 VIP-QTY         PIC 9(2) VALUE ZERO.
          05 PARKING-PASS    PIC X.
             88 WANTS-PARKING VALUE 'Y'.

       01 PRICES.
          05 GA-PRICE        PIC 9(3)V99 VALUE 75.00.
          05 VIP-PRICE       PIC 9(3)V99 VALUE 250.00.
          05 PARKING-FEE     PIC 9(2)V99 VALUE 40.00.

       01 TOTALS.
          05 GA-TOTAL        PIC 9(5)V99 VALUE ZERO.
          05 VIP-TOTAL       PIC 9(5)V99 VALUE ZERO.
          05 PROCESSING-FEE  PIC 9(4)V99 VALUE ZERO.
          05 GRAND-SUM       PIC 9(6)V99 VALUE ZERO.

       01 F-AMT              PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       MAIN-APP.
           DISPLAY "*** SUMMER FESTIVAL BOX OFFICE ***".
           DISPLAY "Ticket Buyer Name: ".
           ACCEPT BUYER-NAME.
           DISPLAY "Quantity of General Admission ($75): ".
           ACCEPT GEN-ADM-QTY.
           DISPLAY "Quantity of VIP Passes ($250): ".
           ACCEPT VIP-QTY.
           DISPLAY "Add VIP Parking Pass ($40)? (Y/N): ".
           ACCEPT PARKING-PASS.

           PERFORM PROCESS-TRANSACTION.
           PERFORM DISPLAY-INVOICE.
           STOP RUN.

       PROCESS-TRANSACTION.
           COMPUTE GA-TOTAL = GEN-ADM-QTY * GA-PRICE.
           COMPUTE VIP-TOTAL = VIP-QTY * VIP-PRICE.
           
           COMPUTE GRAND-SUM = GA-TOTAL + VIP-TOTAL.
           
           IF WANTS-PARKING
               ADD PARKING-FEE TO GRAND-SUM
           END-IF.

           COMPUTE PROCESSING-FEE = GRAND-SUM * 0.08.
           ADD PROCESSING-FEE TO GRAND-SUM.

       DISPLAY-INVOICE.
           DISPLAY " "
           DISPLAY "**************************************"
           DISPLAY "        FESTIVAL TICKET INVOICE       "
           DISPLAY "**************************************"
           DISPLAY "Purchaser: " BUYER-NAME
           DISPLAY "--------------------------------------"
           IF GEN-ADM-QTY > 0
               MOVE GA-TOTAL TO F-AMT
               DISPLAY GEN-ADM-QTY "x General Adm:   " F-AMT
           END-IF
           IF VIP-QTY > 0
               MOVE VIP-TOTAL TO F-AMT
               DISPLAY VIP-QTY "x VIP Pass:      " F-AMT
           END-IF
           IF WANTS-PARKING
               MOVE PARKING-FEE TO F-AMT
               DISPLAY "1x Parking Pass: " F-AMT
           END-IF
           DISPLAY "--------------------------------------"
           MOVE PROCESSING-FEE TO F-AMT.
           DISPLAY "Service Fees(8%):" F-AMT.
           MOVE GRAND-SUM TO F-AMT.
           DISPLAY "TOTAL DUE:       " F-AMT.
           DISPLAY "**************************************".
