       IDENTIFICATION DIVISION.
       PROGRAM-ID. STUDENT-GRADING.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 STUDENT-RECORD.
          05 STUD-ID         PIC 9(6).
          05 STUD-NAME       PIC X(25).
          
       01 SUBJECT-MARKS.
          05 MATH-MARK       PIC 9(3).
          05 SCI-MARK        PIC 9(3).
          05 ENG-MARK        PIC 9(3).
          05 HIST-MARK       PIC 9(3).
          
       01 CALC-RESULTS.
          05 TOTAL-MARKS     PIC 9(4).
          05 AVERAGE-MARK    PIC 9(3)V99.
          05 LETTER-GRADE    PIC X(2).
          05 PASS-FAIL       PIC X(4).
          
       01 PROGRAM-CTRL.
          05 WANT-TO-EXIT    PIC X VALUE 'N'.

       PROCEDURE DIVISION.
       MAIN-ROUTINE.
           DISPLAY "*** STUDENT GRADING SYSTEM ***".
           PERFORM UNTIL WANT-TO-EXIT = 'Y' OR 'y'
               PERFORM INPUT-STUDENT
               PERFORM CALC-GRADES
               PERFORM DISPLAY-REPORT
               DISPLAY "Grade another student? (N/Y): "
               ACCEPT WANT-TO-EXIT
           END-PERFORM.
           DISPLAY "System terminated.".
           STOP RUN.

       INPUT-STUDENT.
           DISPLAY "----------------------------".
           DISPLAY "Enter Student ID: ".
           ACCEPT STUD-ID.
           DISPLAY "Enter Student Name: ".
           ACCEPT STUD-NAME.
           DISPLAY "Enter Math Score (0-100): ".
           ACCEPT MATH-MARK.
           DISPLAY "Enter Science Score (0-100): ".
           ACCEPT SCI-MARK.
           DISPLAY "Enter English Score (0-100): ".
           ACCEPT ENG-MARK.
           DISPLAY "Enter History Score (0-100): ".
           ACCEPT HIST-MARK.

       CALC-GRADES.
           COMPUTE TOTAL-MARKS = MATH-MARK + SCI-MARK + ENG-MARK + 
                                 HIST-MARK.
           COMPUTE AVERAGE-MARK = TOTAL-MARKS / 4.
           
           IF AVERAGE-MARK >= 90
               MOVE "A" TO LETTER-GRADE
               MOVE "PASS" TO PASS-FAIL
           ELSE IF AVERAGE-MARK >= 80
               MOVE "B" TO LETTER-GRADE
               MOVE "PASS" TO PASS-FAIL
           ELSE IF AVERAGE-MARK >= 70
               MOVE "C" TO LETTER-GRADE
               MOVE "PASS" TO PASS-FAIL
           ELSE IF AVERAGE-MARK >= 60
               MOVE "D" TO LETTER-GRADE
               MOVE "PASS" TO PASS-FAIL
           ELSE
               MOVE "F" TO LETTER-GRADE
               MOVE "FAIL" TO PASS-FAIL
           END-IF.

       DISPLAY-REPORT.
           DISPLAY " ".
           DISPLAY "===== ACADEMIC REPORT =====".
           DISPLAY "Student: " STUD-NAME " (" STUD-ID ")".
           DISPLAY "Total Marks:   " TOTAL-MARKS " / 400".
           DISPLAY "Average Score: " AVERAGE-MARK.
           DISPLAY "Final Grade:   " LETTER-GRADE.
           DISPLAY "Status:        " PASS-FAIL.
           DISPLAY "===========================".
