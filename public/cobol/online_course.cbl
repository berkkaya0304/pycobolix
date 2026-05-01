       IDENTIFICATION DIVISION.
       PROGRAM-ID. ONLINE-COURSE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 STUDENT-INFO.
          05 STUD-NAME       PIC X(30).
          05 COURSE-CDE      PIC X.
             88 C-PYTHON     VALUE 'P'.
             88 C-COBOL      VALUE 'C'.
             88 C-JAVA       VALUE 'J'.

       01 UPSELLS.
          05 WANTS-CERT      PIC X.
          05 WANTS-TUTOR     PIC X.
          05 IS-ALUMNI       PIC X.

       01 FEES.
          05 BASE-FEE        PIC 9(4)V99 VALUE ZERO.
          05 CERT-FEE        PIC 9(3)V99 VALUE ZERO.
          05 TUTOR-FEE       PIC 9(3)V99 VALUE ZERO.
          05 DISCOUNT-AMT    PIC 9(4)V99 VALUE ZERO.
          05 FINAL-DUE       PIC 9(5)V99 VALUE ZERO.

       01 DISP-FMT           PIC $ZZZ,ZZ9.99.
       01 COURSE-NAME        PIC X(20).

       PROCEDURE DIVISION.
       MAIN-PROC.
           DISPLAY "--- E-LEARNING REGISTRATION ---".
           DISPLAY "Student Name: ".
           ACCEPT STUD-NAME.
           DISPLAY "Course (P=Python, C=COBOL, J=Java): ".
           ACCEPT COURSE-CDE.
           DISPLAY "Add Verified Certificate ($50)? (Y/N): ".
           ACCEPT WANTS-CERT.
           DISPLAY "Add 1-on-1 Tutoring ($150)? (Y/N): ".
           ACCEPT WANTS-TUTOR.
           DISPLAY "Are you a returning alumni (10% off)? (Y/N): ".
           ACCEPT IS-ALUMNI.

           PERFORM PROCESS-REG.
           PERFORM PRINT-INVOICE.
           STOP RUN.

       PROCESS-REG.
           EVALUATE TRUE
               WHEN C-PYTHON
                   MOVE 200.00 TO BASE-FEE
                   MOVE "Python Masterclass" TO COURSE-NAME
               WHEN C-COBOL
                   MOVE 500.00 TO BASE-FEE
                   MOVE "Legacy Sys COBOL" TO COURSE-NAME
               WHEN C-JAVA
                   MOVE 300.00 TO BASE-FEE
                   MOVE "Java Fundamentals" TO COURSE-NAME
               WHEN OTHER
                   MOVE 200.00 TO BASE-FEE
                   MOVE "Default Course" TO COURSE-NAME
           END-EVALUATE.

           IF WANTS-CERT = 'Y' OR 'y'
               MOVE 50.00 TO CERT-FEE
           END-IF.

           IF WANTS-TUTOR = 'Y' OR 'y'
               MOVE 150.00 TO TUTOR-FEE
           END-IF.

           IF IS-ALUMNI = 'Y' OR 'y'
               COMPUTE DISCOUNT-AMT = BASE-FEE * 0.10
           END-IF.

           COMPUTE FINAL-DUE = BASE-FEE + CERT-FEE + TUTOR-FEE 
                             - DISCOUNT-AMT.

       PRINT-INVOICE.
           DISPLAY " "
           DISPLAY "======================================"
           DISPLAY "      COURSE ENROLLMENT RECEIPT       "
           DISPLAY "======================================"
           DISPLAY "Student: " STUD-NAME.
           DISPLAY "Course:  " COURSE-NAME.
           DISPLAY "--------------------------------------"
           MOVE BASE-FEE TO DISP-FMT.
           DISPLAY "Tuition Fee:      " DISP-FMT.
           
           IF CERT-FEE > 0
               MOVE CERT-FEE TO DISP-FMT
               DISPLAY "Certificate Fee:  " DISP-FMT
           END-IF.
           
           IF TUTOR-FEE > 0
               MOVE TUTOR-FEE TO DISP-FMT
               DISPLAY "Tutoring Add-on:  " DISP-FMT
           END-IF.

           IF DISCOUNT-AMT > 0
               MOVE DISCOUNT-AMT TO DISP-FMT
               DISPLAY "Alumni Discount: -" DISP-FMT
           END-IF.
           DISPLAY "--------------------------------------"
           MOVE FINAL-DUE TO DISP-FMT.
           DISPLAY "TOTAL ENROLLMENT: " DISP-FMT.
           DISPLAY "======================================".
