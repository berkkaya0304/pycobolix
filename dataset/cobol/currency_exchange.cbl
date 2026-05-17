       IDENTIFICATION DIVISION.
       PROGRAM-ID. CURRENCY-EXCHANGE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 USER-INPUT.
          05 CUST-NAME       PIC X(20).
          05 CURRENCY-FROM   PIC X(3).
          05 CURRENCY-TO     PIC X(3).
          05 AMOUNT-TO-EXCH  PIC 9(7)V99.

       01 EXCHANGE-RATES.
          05 RATE-USD-EUR    PIC 9V9999 VALUE 0.9250.
          05 RATE-USD-GBP    PIC 9V9999 VALUE 0.7930.
          05 RATE-EUR-USD    PIC 9V9999 VALUE 1.0810.
          05 RATE-GBP-USD    PIC 9V9999 VALUE 1.2610.

       01 CALCULATIONS.
          05 CONV-RATE       PIC 9V9999 VALUE 1.0000.
          05 CONV-AMOUNT     PIC 9(7)V99 VALUE ZERO.
          05 COMM-FEE        PIC 9(4)V99 VALUE ZERO.
          05 FINAL-PAYOUT    PIC 9(7)V99 VALUE ZERO.
          
       01 DISP-FMT           PIC Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-EXCHANGE.
           DISPLAY "--- GLOBAL CURRENCY EXCHANGE ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Source Currency (USD/EUR/GBP): ".
           ACCEPT CURRENCY-FROM.
           DISPLAY "Target Currency (USD/EUR/GBP): ".
           ACCEPT CURRENCY-TO.
           DISPLAY "Amount to Exchange: ".
           ACCEPT AMOUNT-TO-EXCH.

           PERFORM PROCESS-CONVERSION.
           PERFORM PRINT-RECEIPT.
           STOP RUN.

       PROCESS-CONVERSION.
           IF CURRENCY-FROM = "USD" AND CURRENCY-TO = "EUR"
               MOVE RATE-USD-EUR TO CONV-RATE
           ELSE IF CURRENCY-FROM = "USD" AND CURRENCY-TO = "GBP"
               MOVE RATE-USD-GBP TO CONV-RATE
           ELSE IF CURRENCY-FROM = "EUR" AND CURRENCY-TO = "USD"
               MOVE RATE-EUR-USD TO CONV-RATE
           ELSE IF CURRENCY-FROM = "GBP" AND CURRENCY-TO = "USD"
               MOVE RATE-GBP-USD TO CONV-RATE
           ELSE
               DISPLAY "Exchange route not supported. Rate = 1.0"
               MOVE 1.0000 TO CONV-RATE
           END-IF.

           COMPUTE CONV-AMOUNT = AMOUNT-TO-EXCH * CONV-RATE.
           
           COMPUTE COMM-FEE = CONV-AMOUNT * 0.02.
           COMPUTE FINAL-PAYOUT = CONV-AMOUNT - COMM-FEE.

       PRINT-RECEIPT.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "        FOREX EXCHANGE RECEIPT           "
           DISPLAY "========================================="
           DISPLAY "Customer:      " CUST-NAME
           DISPLAY "Exchange Path: " CURRENCY-FROM " to " CURRENCY-TO
           DISPLAY "Exchange Rate: " CONV-RATE
           DISPLAY "-----------------------------------------"
           MOVE AMOUNT-TO-EXCH TO DISP-FMT.
           DISPLAY "Input Amount:  " DISP-FMT " " CURRENCY-FROM.
           MOVE CONV-AMOUNT TO DISP-FMT.
           DISPLAY "Gross Converted: " DISP-FMT " " CURRENCY-TO.
           MOVE COMM-FEE TO DISP-FMT.
           DISPLAY "Commission (2%):-" DISP-FMT " " CURRENCY-TO.
           DISPLAY "-----------------------------------------"
           MOVE FINAL-PAYOUT TO DISP-FMT.
           DISPLAY "FINAL PAYOUT:   " DISP-FMT " " CURRENCY-TO.
           DISPLAY "=========================================".
