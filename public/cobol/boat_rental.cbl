       IDENTIFICATION DIVISION.
       PROGRAM-ID. BOAT-RENTAL.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CHARTER-INFO.
          05 CUSTOMER        PIC X(20).
          05 BOAT-TYPE       PIC 9.
             88 KAYAK        VALUE 1.
             88 PONTOON      VALUE 2.
             88 SPEEDBOAT    VALUE 3.
          05 HOURS-RENT      PIC 9(2).
          05 LIFE-JACKETS    PIC 9(2).

       01 FEES.
          05 HOURLY-RATE     PIC 9(3)V99 VALUE ZERO.
          05 BOAT-TOTAL      PIC 9(4)V99 VALUE ZERO.
          05 JACKET-FEE      PIC 9(3)V99 VALUE ZERO.
          05 INSUR-FEE       PIC 9(3)V99 VALUE 25.00.
          05 GROSS-AMT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-RENTAL.
           DISPLAY "--- LAKESIDE MARINA RENTALS ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUSTOMER.
           DISPLAY "Boat (1=Kayak $15/h, 2=Pontoon $75, 3=Speed $120): ".
           ACCEPT BOAT-TYPE.
           DISPLAY "Rental Duration (Hours): ".
           ACCEPT HOURS-RENT.
           DISPLAY "Extra Life Jackets Needed ($5 flat ea): ".
           ACCEPT LIFE-JACKETS.

           EVALUATE TRUE
               WHEN KAYAK
                   MOVE 15.00 TO HOURLY-RATE
                   MOVE ZERO TO INSUR-FEE
               WHEN PONTOON
                   MOVE 75.00 TO HOURLY-RATE
               WHEN SPEEDBOAT
                   MOVE 120.00 TO HOURLY-RATE
               WHEN OTHER
                   MOVE 15.00 TO HOURLY-RATE
                   MOVE ZERO TO INSUR-FEE
           END-EVALUATE.

           COMPUTE BOAT-TOTAL = HOURS-RENT * HOURLY-RATE.
           COMPUTE JACKET-FEE = LIFE-JACKETS * 5.00.
           
           COMPUTE GROSS-AMT = BOAT-TOTAL + JACKET-FEE + INSUR-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          MARINA RENTAL AGREEMENT       "
           DISPLAY "========================================"
           DISPLAY "Renter: " CUSTOMER
           DISPLAY "Duration: " HOURS-RENT " hours"
           DISPLAY "----------------------------------------"
           MOVE BOAT-TOTAL TO DISP.
           DISPLAY "Vessel Rental Fee:  " DISP.
           
           IF JACKET-FEE > 0
               MOVE JACKET-FEE TO DISP
               DISPLAY "Life Jacket Rental: " DISP
           END-IF.
           
           IF INSUR-FEE > 0
               MOVE INSUR-FEE TO DISP
               DISPLAY "Damage Insurance:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GROSS-AMT TO DISP.
           DISPLAY "TOTAL BALANCE DUE:  " DISP.
           DISPLAY "========================================".
           STOP RUN.
