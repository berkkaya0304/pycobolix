       IDENTIFICATION DIVISION.
       PROGRAM-ID. LANGUAGE-TUTOR.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 STUDENT-INFO.
          05 STUDENT-NAME    PIC X(20).
          05 LANG-CHOSEN     PIC 9.
             88 SPANISH      VALUE 1.
             88 FRENCH       VALUE 2.
             88 MANDARIN     VALUE 3.
          05 LEVEL-TIER      PIC 9.
             88 BEGINNER     VALUE 1.
             88 ADVANCED     VALUE 2.
          05 HOURS-REQ       PIC 9(2)V9.

       01 CALCS.
          05 BASE-HOURLY     PIC 9(2)V99 VALUE ZERO.
          05 LEVEL-SURCHG    PIC 9(2)V99 VALUE ZERO.
          05 FINAL-HOURLY    PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-COST      PIC 9(4)V99 VALUE ZERO.
          05 DISCOUNT        PIC 9(3)V99 VALUE ZERO.
          05 NET-PAYABLE     PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-TUTOR.
           DISPLAY "--- GLOBAL VOICES TUTORING ---".
           DISPLAY "Student Name: ".
           ACCEPT STUDENT-NAME.
           DISPLAY "Language (1=Spanish $30/hr, 2=French $35/hr, ".
           DISPLAY "          3=Mandarin $45/hr): ".
           ACCEPT LANG-CHOSEN.
           DISPLAY "Level (1=Beginner, 2=Advanced +$10/hr): ".
           ACCEPT LEVEL-TIER.
           DISPLAY "Hours per week requested: ".
           ACCEPT HOURS-REQ.

           EVALUATE TRUE
               WHEN SPANISH
                   MOVE 30.00 TO BASE-HOURLY
               WHEN FRENCH
                   MOVE 35.00 TO BASE-HOURLY
               WHEN MANDARIN
                   MOVE 45.00 TO BASE-HOURLY
               WHEN OTHER
                   MOVE 30.00 TO BASE-HOURLY
           END-EVALUATE.

           IF ADVANCED
               MOVE 10.00 TO LEVEL-SURCHG
           END-IF.

           COMPUTE FINAL-HOURLY = BASE-HOURLY + LEVEL-SURCHG.
           COMPUTE TOTAL-COST = HOURS-REQ * FINAL-HOURLY.

           IF HOURS-REQ >= 5.0
               COMPUTE DISCOUNT = TOTAL-COST * 0.10
           END-IF.

           COMPUTE NET-PAYABLE = TOTAL-COST - DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          TUTORING INVOICE              "
           DISPLAY "========================================"
           DISPLAY "Student: " STUDENT-NAME
           DISPLAY "Hours:   " HOURS-REQ " / week"
           DISPLAY "----------------------------------------"
           MOVE FINAL-HOURLY TO DISP.
           DISPLAY "Hourly Rate Applied: " DISP.
           MOVE TOTAL-COST TO DISP.
           DISPLAY "Gross Weekly Cost:   " DISP.
           
           IF DISCOUNT > 0
               MOVE DISCOUNT TO DISP
               DISPLAY "Volume Discount:    -" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE NET-PAYABLE TO DISP.
           DISPLAY "NET WEEKLY PAYABLE:  " DISP.
           DISPLAY "========================================".
           STOP RUN.
