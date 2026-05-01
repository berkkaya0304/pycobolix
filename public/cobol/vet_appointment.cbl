       IDENTIFICATION DIVISION.
       PROGRAM-ID. VET-APPOINTMENT.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 APPT-INFO.
          05 PET-NAME        PIC X(20).
          05 VISIT-REASON    PIC 9.
             88 WELLNESS     VALUE 1.
             88 SICK         VALUE 2.
             88 EMERGENCY    VALUE 3.
          05 DOCTOR-REQ      PIC 9.
             88 DR-SMITH     VALUE 1.
             88 DR-JONES     VALUE 2.

       01 FEES.
          05 EXAM-FEE        PIC 9(3)V99 VALUE ZERO.
          05 DR-SURCHARGE    PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-ESTIMATE  PIC 9(4)V99 VALUE ZERO.

       01 DISP-VAL           PIC $Z,ZZ9.99.
       01 REASON-TXT         PIC X(20).
       01 DR-TXT             PIC X(20).

       PROCEDURE DIVISION.
       START-SCHED.
           DISPLAY "--- VET CLINIC SCHEDULING ---".
           DISPLAY "Pet Name: ".
           ACCEPT PET-NAME.
           DISPLAY "Reason for Visit: ".
           DISPLAY "1=Wellness Exam ($50)".
           DISPLAY "2=Sick Visit ($85)".
           DISPLAY "3=Emergency ($150)".
           ACCEPT VISIT-REASON.
           
           DISPLAY "Requested Doctor: ".
           DISPLAY "1=Dr. Smith (General)".
           DISPLAY "2=Dr. Jones (Specialist +$40)".
           ACCEPT DOCTOR-REQ.

           PERFORM CALC-ESTIMATE.
           PERFORM PRINT-CONFIRMATION.
           STOP RUN.

       CALC-ESTIMATE.
           EVALUATE TRUE
               WHEN WELLNESS
                   MOVE 50.00 TO EXAM-FEE
                   MOVE "Wellness Exam" TO REASON-TXT
               WHEN SICK
                   MOVE 85.00 TO EXAM-FEE
                   MOVE "Sick Visit" TO REASON-TXT
               WHEN EMERGENCY
                   MOVE 150.00 TO EXAM-FEE
                   MOVE "Emergency" TO REASON-TXT
               WHEN OTHER
                   MOVE 50.00 TO EXAM-FEE
                   MOVE "Wellness (Default)" TO REASON-TXT
           END-EVALUATE.

           EVALUATE TRUE
               WHEN DR-SMITH
                   MOVE ZERO TO DR-SURCHARGE
                   MOVE "Dr. Smith" TO DR-TXT
               WHEN DR-JONES
                   MOVE 40.00 TO DR-SURCHARGE
                   MOVE "Dr. Jones" TO DR-TXT
               WHEN OTHER
                   MOVE ZERO TO DR-SURCHARGE
                   MOVE "Any Available" TO DR-TXT
           END-EVALUATE.

           COMPUTE TOTAL-ESTIMATE = EXAM-FEE + DR-SURCHARGE.

       PRINT-CONFIRMATION.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "       APPOINTMENT CONFIRMATION         "
           DISPLAY "========================================"
           DISPLAY "Patient: " PET-NAME
           DISPLAY "Doctor:  " DR-TXT
           DISPLAY "Visit:   " REASON-TXT
           DISPLAY "----------------------------------------"
           MOVE EXAM-FEE TO DISP-VAL.
           DISPLAY "Base Exam Fee:      " DISP-VAL.
           IF DR-SURCHARGE > 0
               MOVE DR-SURCHARGE TO DISP-VAL
               DISPLAY "Specialist Fee:     " DISP-VAL
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-ESTIMATE TO DISP-VAL.
           DISPLAY "ESTIMATED TOTAL:    " DISP-VAL.
           DISPLAY "=======================================".
