       IDENTIFICATION DIVISION.
       PROGRAM-ID. TRAIN-TICKET.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PASSENGER-REC.
          05 PASSENGER-NAME  PIC X(25).
          05 AGE             PIC 9(3).
          05 DISTANCE-KM     PIC 9(4).
          05 CLASS-TYPE      PIC X.
             88 AC-FIRST     VALUE '1'.
             88 AC-SECOND    VALUE '2'.
             88 SLEEPER      VALUE 'S'.
             88 GENERAL-C    VALUE 'G'.

       01 COSTS.
          05 BASE-FARE       PIC 9(4)V99 VALUE ZERO.
          05 CONCESSION      PIC 9(3)V99 VALUE ZERO.
          05 RESERVATION-FEE PIC 9(2)V99 VALUE 20.00.
          05 TOTAL-FARE      PIC 9(5)V99 VALUE ZERO.

       01 DISP-FMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       APP-ENTRY.
           DISPLAY "--- RAILWAY TICKET BOOKING ---".
           DISPLAY "Passenger Name: ".
           ACCEPT PASSENGER-NAME.
           DISPLAY "Passenger Age: ".
           ACCEPT AGE.
           DISPLAY "Travel Distance (KM): ".
           ACCEPT DISTANCE-KM.
           DISPLAY "Class (1=1AC, 2=2AC, S=Sleeper, G=General): ".
           ACCEPT CLASS-TYPE.

           PERFORM FARE-CALC.
           PERFORM ISSUE-TICKET.
           STOP RUN.

       FARE-CALC.
           EVALUATE TRUE
               WHEN AC-FIRST
                   COMPUTE BASE-FARE = DISTANCE-KM * 3.50
               WHEN AC-SECOND
                   COMPUTE BASE-FARE = DISTANCE-KM * 2.00
               WHEN SLEEPER
                   COMPUTE BASE-FARE = DISTANCE-KM * 1.00
               WHEN GENERAL-C
                   COMPUTE BASE-FARE = DISTANCE-KM * 0.50
                   MOVE ZERO TO RESERVATION-FEE
               WHEN OTHER
                   COMPUTE BASE-FARE = DISTANCE-KM * 0.50
                   MOVE ZERO TO RESERVATION-FEE
           END-EVALUATE.

           IF AGE >= 60
               COMPUTE CONCESSION = BASE-FARE * 0.40
           ELSE IF AGE <= 12
               COMPUTE CONCESSION = BASE-FARE * 0.50
           END-IF.

           COMPUTE TOTAL-FARE = BASE-FARE + RESERVATION-FEE - CONCESSION.

       ISSUE-TICKET.
           DISPLAY " "
           DISPLAY "==========================================="
           DISPLAY "          E-TICKET CONFIRMATION            "
           DISPLAY "==========================================="
           DISPLAY "Name: " PASSENGER-NAME "   Age: " AGE " yrs"
           DISPLAY "Distance: " DISTANCE-KM " km"
           DISPLAY "-------------------------------------------"
           MOVE BASE-FARE TO DISP-FMT.
           DISPLAY "Base Distance Fare: " DISP-FMT.
           
           IF RESERVATION-FEE > 0
               MOVE RESERVATION-FEE TO DISP-FMT
               DISPLAY "Reservation Fee:    " DISP-FMT
           END-IF.
           
           IF CONCESSION > 0
               MOVE CONCESSION TO DISP-FMT
               DISPLAY "Age Concession:    -" DISP-FMT
           END-IF.
           DISPLAY "-------------------------------------------"
           MOVE TOTAL-FARE TO DISP-FMT.
           DISPLAY "TOTAL FARE PAYABLE: " DISP-FMT.
           DISPLAY "===========================================".
