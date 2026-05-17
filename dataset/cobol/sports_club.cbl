       IDENTIFICATION DIVISION.
       PROGRAM-ID. SPORTS-CLUB.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MEMBERSHIP-REC.
          05 MEMBER-NAME     PIC X(25).
          05 SPORT-DEPT      PIC X.
             88 TENNIS       VALUE 'T'.
             88 GOLF         VALUE 'G'.
             88 SWIMMING     VALUE 'S'.
          05 MONTHS-MBR      PIC 9(2) VALUE 1.
          05 EQUIPMENT-RNT   PIC X.
             88 RENT-EQUIP   VALUE 'Y'.

       01 BILL-CALCS.
          05 REGISTRY-FEE    PIC 9(3)V99 VALUE 150.00.
          05 MONTHLY-FEE     PIC 9(3)V99 VALUE ZERO.
          05 EQUIP-FEE       PIC 9(3)V99 VALUE ZERO.
          05 SUB-TOTAL       PIC 9(5)V99.
          05 TOTAL-BILL      PIC 9(5)V99.

       01 C-FMT              PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-PGM.
           DISPLAY "--- ELITE SPORTS CLUB REGISTRATION ---".
           DISPLAY "Member Name: ".
           ACCEPT MEMBER-NAME.
           DISPLAY "Sport (T=Tennis, G=Golf, S=Swimming): ".
           ACCEPT SPORT-DEPT.
           DISPLAY "Months to prepay (1-12): ".
           ACCEPT MONTHS-MBR.
           DISPLAY "Rent Club Equipment ($30/mo)? (Y/N): ".
           ACCEPT EQUIPMENT-RNT.

           PERFORM PROCESS-REGISTRATION.
           PERFORM OUTPUT-INVOICE.
           STOP RUN.

       PROCESS-REGISTRATION.
           EVALUATE TRUE
               WHEN TENNIS
                   MOVE 100.00 TO MONTHLY-FEE
               WHEN GOLF
                   MOVE 250.00 TO MONTHLY-FEE
               WHEN SWIMMING
                   MOVE 75.00 TO MONTHLY-FEE
               WHEN OTHER
                   MOVE 100.00 TO MONTHLY-FEE
           END-EVALUATE.

           IF RENT-EQUIP
               MOVE 30.00 TO EQUIP-FEE
           END-IF.

           COMPUTE SUB-TOTAL = (MONTHLY-FEE * MONTHS-MBR) 
                             + (EQUIP-FEE * MONTHS-MBR).
                             
           COMPUTE TOTAL-BILL = SUB-TOTAL + REGISTRY-FEE.

       OUTPUT-INVOICE.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "           CLUB MEMBERSHIP             "
           DISPLAY "======================================="
           DISPLAY "Welcome, " MEMBER-NAME
           DISPLAY "Prepaid Term: " MONTHS-MBR " months"
           DISPLAY "---------------------------------------"
           MOVE REGISTRY-FEE TO C-FMT.
           DISPLAY "One-Time Joining Fee: " C-FMT.
           
           MULTIPLY MONTHLY-FEE BY MONTHS-MBR GIVING MONTHLY-FEE.
           MOVE MONTHLY-FEE TO C-FMT.
           DISPLAY "Membership Dues:      " C-FMT.
           
           IF RENT-EQUIP
               MULTIPLY EQUIP-FEE BY MONTHS-MBR GIVING EQUIP-FEE
               MOVE EQUIP-FEE TO C-FMT
               DISPLAY "Equipment Rental:     " C-FMT
           END-IF.
           DISPLAY "---------------------------------------"
           MOVE TOTAL-BILL TO C-FMT.
           DISPLAY "TOTAL REGISTRATION:   " C-FMT.
           DISPLAY "=======================================".
