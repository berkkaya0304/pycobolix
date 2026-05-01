       IDENTIFICATION DIVISION.
       PROGRAM-ID. EMPLOYEE-EVALUATION.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 EMP-RECORD.
          05 EMP-ID          PIC X(6).
          05 EMP-NAME        PIC X(25).
          05 BASE-SALARY     PIC 9(6)V99.
          
       01 EVAL-SCORES.
          05 PROD-SCORE      PIC 9(3).
          05 TEAM-SCORE      PIC 9(3).
          05 QUAL-SCORE      PIC 9(3).
          05 TOTAL-SCORE     PIC 9(4).
          05 AVG-SCORE       PIC 9(3)V99.

       01 BONUS-CALC.
          05 BONUS-PCT       PIC V99 VALUE ZERO.
          05 BONUS-AMT       PIC 9(6)V99 VALUE ZERO.
          05 NEW-COMP        PIC 9(7)V99 VALUE ZERO.

       01 DISPLAY-VARS.
          05 FMT-SALARY      PIC $Z,ZZZ,ZZ9.99.
          05 RATING-TXT      PIC X(15).
          05 EVAL-LOOP       PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       MAIN-LOGIC.
           DISPLAY "--- ANNUAL HR EVALUATION SCHEME ---".
           PERFORM UNTIL EVAL-LOOP = 'N' OR 'n'
               PERFORM GET-EMP-DATA
               PERFORM CALC-SCORES
               PERFORM CALC-BONUS
               PERFORM SHOW-RESULTS
               DISPLAY "Evaluate another employee? (Y/N): "
               ACCEPT EVAL-LOOP
           END-PERFORM.
           STOP RUN.

       GET-EMP-DATA.
           DISPLAY "Employee ID: ".
           ACCEPT EMP-ID.
           DISPLAY "Employee Name: ".
           ACCEPT EMP-NAME.
           DISPLAY "Current Base Salary ($): ".
           ACCEPT BASE-SALARY.
           DISPLAY "Productivity Score (0-100): ".
           ACCEPT PROD-SCORE.
           DISPLAY "Teamwork Score (0-100): ".
           ACCEPT TEAM-SCORE.
           DISPLAY "Quality of Work Score (0-100): ".
           ACCEPT QUAL-SCORE.

       CALC-SCORES.
           COMPUTE TOTAL-SCORE = PROD-SCORE + TEAM-SCORE + QUAL-SCORE.
           COMPUTE AVG-SCORE = TOTAL-SCORE / 3.
           
           IF AVG-SCORE >= 90
               MOVE "OUTSTANDING" TO RATING-TXT
               MOVE .15 TO BONUS-PCT
           ELSE IF AVG-SCORE >= 80
               MOVE "EXCEEDS ELIG" TO RATING-TXT
               MOVE .10 TO BONUS-PCT
           ELSE IF AVG-SCORE >= 70
               MOVE "MEETS ELIG" TO RATING-TXT
               MOVE .05 TO BONUS-PCT
           ELSE
               MOVE "NEEDS IMPRV" TO RATING-TXT
               MOVE .00 TO BONUS-PCT
           END-IF.

       CALC-BONUS.
           COMPUTE BONUS-AMT = BASE-SALARY * BONUS-PCT.
           COMPUTE NEW-COMP = BASE-SALARY + BONUS-AMT.

       SHOW-RESULTS.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "      PERFORMANCE REVIEW SUMMARY        "
           DISPLAY "========================================"
           DISPLAY "Employee: " EMP-NAME " (" EMP-ID ")"
           DISPLAY "----------------------------------------"
           DISPLAY "Productivity: " PROD-SCORE
           DISPLAY "Teamwork:     " TEAM-SCORE
           DISPLAY "Quality:      " QUAL-SCORE
           DISPLAY "Average:      " AVG-SCORE
           DISPLAY "Overall Rating: " RATING-TXT
           DISPLAY "----------------------------------------"
           MOVE BASE-SALARY TO FMT-SALARY.
           DISPLAY "Base Salary:    " FMT-SALARY.
           MOVE BONUS-AMT TO FMT-SALARY.
           DISPLAY "Earned Bonus:   " FMT-SALARY.
           DISPLAY "========================================"
           MOVE NEW-COMP TO FMT-SALARY.
           DISPLAY "TOTAL PACKAGE:  " FMT-SALARY.
           DISPLAY "========================================".
