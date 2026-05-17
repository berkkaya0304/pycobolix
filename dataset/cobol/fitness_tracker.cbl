       IDENTIFICATION DIVISION.
       PROGRAM-ID. FITNESS-TRACKER.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 USER-PROFILE.
          05 USER-NAME       PIC X(20).
          05 WEIGHT-LBS      PIC 9(3).
          05 HEIGHT-IN       PIC 9(3).
          05 DAILY-STEPS     PIC 9(5).
          05 ACTIVITY-LEVEL  PIC 9.
             88 SEDENTARY    VALUE 1.
             88 ACTIVE       VALUE 2.
             88 HIGHLY-ACTIVE VALUE 3.

       01 CALCULATIONS.
          05 BMI-SCORE       PIC 9(3)V9.
          05 CALS-BURNED     PIC 9(4).
          05 BASELINE-BMR    PIC 9(4).
          05 TOTAL-CALS      PIC 9(4).

       01 DISP-NUM           PIC ZZZ,ZZ9.

       PROCEDURE DIVISION.
       START-APP.
           DISPLAY "--- DAILY FITNESS TRACKER ---".
           DISPLAY "User Name: ".
           ACCEPT USER-NAME.
           DISPLAY "Weight (lbs): ".
           ACCEPT WEIGHT-LBS.
           DISPLAY "Height (inches): ".
           ACCEPT HEIGHT-IN.
           DISPLAY "Steps taken today: ".
           ACCEPT DAILY-STEPS.
           DISPLAY "Activity (1=Sedentary, 2=Active, 3=Pro): ".
           ACCEPT ACTIVITY-LEVEL.

           PERFORM COMPUTE-METRICS.
           PERFORM PRINT-DASHBOARD.
           STOP RUN.

       COMPUTE-METRICS.
           COMPUTE BMI-SCORE = (WEIGHT-LBS / (HEIGHT-IN * HEIGHT-IN)) 
                             * 703.

           COMPUTE BASELINE-BMR = WEIGHT-LBS * 11.

           COMPUTE CALS-BURNED = DAILY-STEPS * 0.04.

           EVALUATE TRUE
               WHEN SEDENTARY
                   COMPUTE TOTAL-CALS = BASELINE-BMR * 1.2
               WHEN ACTIVE
                   COMPUTE TOTAL-CALS = BASELINE-BMR * 1.5
               WHEN HIGHLY-ACTIVE
                   COMPUTE TOTAL-CALS = BASELINE-BMR * 1.8
               WHEN OTHER
                   COMPUTE TOTAL-CALS = BASELINE-BMR * 1.2
           END-EVALUATE.

           ADD CALS-BURNED TO TOTAL-CALS.

       PRINT-DASHBOARD.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "         FITNESS DASHBOARD             "
           DISPLAY "======================================="
           DISPLAY "Hello, " USER-NAME "!"
           DISPLAY "---------------------------------------"
           DISPLAY "BMI Score:     " BMI-SCORE.
           IF BMI-SCORE < 18.5
               DISPLAY "Category:      Underweight"
           ELSE IF BMI-SCORE < 25.0
               DISPLAY "Category:      Normal Weight"
           ELSE IF BMI-SCORE < 30.0
               DISPLAY "Category:      Overweight"
           ELSE
               DISPLAY "Category:      Obese"
           END-IF.
           DISPLAY "---------------------------------------"
           DISPLAY "Steps Today:   " DAILY-STEPS.
           MOVE CALS-BURNED TO DISP-NUM.
           DISPLAY "Active Cals Burned: " DISP-NUM.
           MOVE TOTAL-CALS TO DISP-NUM.
           DISPLAY "Total TDEE Cals:    " DISP-NUM.
           DISPLAY "=======================================".
