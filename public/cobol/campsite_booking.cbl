       IDENTIFICATION DIVISION.
       PROGRAM-ID. CAMPSITE-BOOKING.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CAMP-RESERVE.
          05 CAMPER-NAME     PIC X(20).
          05 SITE-TYPE       PIC 9.
             88 TENT-SITE    VALUE 1.
             88 RV-SITE      VALUE 2.
             88 CABIN        VALUE 3.
          05 STAY-NIGHTS     PIC 9(2).
          05 FIREWOOD-BNDL   PIC 9(2) VALUE ZERO.

       01 FEES.
          05 SITE-RATE       PIC 9(3)V99 VALUE ZERO.
          05 SITE-TOTAL      PIC 9(4)V99 VALUE ZERO.
          05 WOOD-FEE        PIC 9(3)V99 VALUE ZERO.
          05 PARK-PASS       PIC 9(2)V99 VALUE 15.00.
          05 TOTAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-BOOKING.
           DISPLAY "--- PINE RIDGE CAMPGROUND ---".
           DISPLAY "Camper Name: ".
           ACCEPT CAMPER-NAME.
           DISPLAY "Site (1=Tent $20, 2=RV Hookup $50, 3=Cabin $100): ".
           ACCEPT SITE-TYPE.
           DISPLAY "Number of Nights: ".
           ACCEPT STAY-NIGHTS.
           DISPLAY "Firewood Bundles ($8 ea): ".
           ACCEPT FIREWOOD-BNDL.

           EVALUATE TRUE
               WHEN TENT-SITE
                   MOVE 20.00 TO SITE-RATE
               WHEN RV-SITE
                   MOVE 50.00 TO SITE-RATE
               WHEN CABIN
                   MOVE 100.00 TO SITE-RATE
               WHEN OTHER
                   MOVE 20.00 TO SITE-RATE
           END-EVALUATE.

           COMPUTE SITE-TOTAL = STAY-NIGHTS * SITE-RATE.
           COMPUTE WOOD-FEE = FIREWOOD-BNDL * 8.00.

           COMPUTE TOTAL-BILL = SITE-TOTAL + WOOD-FEE + PARK-PASS.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          CAMPGROUND RESERVATION        "
           DISPLAY "========================================"
           DISPLAY "Camper: " CAMPER-NAME
           DISPLAY "Nights: " STAY-NIGHTS
           DISPLAY "----------------------------------------"
           MOVE SITE-TOTAL TO DISP.
           DISPLAY "Site Reservation Fee:   " DISP.
           
           IF FIREWOOD-BNDL > 0
               MOVE WOOD-FEE TO DISP
               DISPLAY "Firewood (" FIREWOOD-BNDL " bundles):   " DISP
           END-IF.
           
           MOVE PARK-PASS TO DISP.
           DISPLAY "State Park Entry Pass:  " DISP.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-BILL TO DISP.
           DISPLAY "TOTAL BALANCE DUE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
