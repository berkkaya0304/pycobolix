       IDENTIFICATION DIVISION.
       PROGRAM-ID. PATIENT-BILLING.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PATIENT-REC.
          05 PAT-ID          PIC X(8).
          05 PAT-NAME        PIC X(25).
          05 ADMIT-DAYS      PIC 9(3).
          05 ROOM-TYPE       PIC 9.
             88 WARD           VALUE 1.
             88 SEMI-PRIVATE   VALUE 2.
             88 PRIVATE-ROOM   VALUE 3.
             
       01 CHARGES.
          05 ROOM-CHG        PIC 9(5)V99 VALUE ZERO.
          05 SURGERY-CHG     PIC 9(6)V99.
          05 MEDICATION-CHG  PIC 9(5)V99.
          05 TOTAL-CHG       PIC 9(7)V99.
          05 INSUR-COVER     PIC 9(7)V99.
          05 PATIENT-OWES    PIC 9(7)V99.

       01 FORM-VAL           PIC $$$,$$$,$$9.99.

       PROCEDURE DIVISION.
       MAIN-ROUTINE.
           DISPLAY "+++ GENERAL HOSPITAL BILLING +++".
           PERFORM INPUT-PHASE.
           PERFORM PROCESS-PHASE.
           PERFORM OUTPUT-PHASE.
           DISPLAY "Billing cycle complete.".
           STOP RUN.

       INPUT-PHASE.
           DISPLAY "Patient ID: ".
           ACCEPT PAT-ID.
           DISPLAY "Patient Name: ".
           ACCEPT PAT-NAME.
           DISPLAY "Days Admitted: ".
           ACCEPT ADMIT-DAYS.
           DISPLAY "Room Type (1=Ward, 2=Semi, 3=Private): ".
           ACCEPT ROOM-TYPE.
           DISPLAY "Surgery Charges ($): ".
           ACCEPT SURGERY-CHG.
           DISPLAY "Medication Charges ($): ".
           ACCEPT MEDICATION-CHG.

       PROCESS-PHASE.
           EVALUATE TRUE
               WHEN WARD
                   COMPUTE ROOM-CHG = ADMIT-DAYS * 150.00
               WHEN SEMI-PRIVATE
                   COMPUTE ROOM-CHG = ADMIT-DAYS * 250.00
               WHEN PRIVATE-ROOM
                   COMPUTE ROOM-CHG = ADMIT-DAYS * 400.00
               WHEN OTHER
                   COMPUTE ROOM-CHG = ADMIT-DAYS * 150.00
                   DISPLAY "(Defaulted room to Ward)"
           END-EVALUATE.

           COMPUTE TOTAL-CHG = ROOM-CHG + SURGERY-CHG + MEDICATION-CHG.
           
           COMPUTE INSUR-COVER = TOTAL-CHG * 0.80.
           COMPUTE PATIENT-OWES = TOTAL-CHG - INSUR-COVER.

       OUTPUT-PHASE.
           DISPLAY " "
           DISPLAY "-----------------------------------------".
           DISPLAY " HOSPITAL DISCHARGE BILL".
           DISPLAY "-----------------------------------------".
           DISPLAY "Patient: " PAT-NAME "  [ID: " PAT-ID "]".
           DISPLAY "Days in Hospital: " ADMIT-DAYS.
           
           MOVE ROOM-CHG TO FORM-VAL.
           DISPLAY "Room Charges:    " FORM-VAL.
           MOVE SURGERY-CHG TO FORM-VAL.
           DISPLAY "Surgery:         " FORM-VAL.
           MOVE MEDICATION-CHG TO FORM-VAL.
           DISPLAY "Medication:      " FORM-VAL.
           DISPLAY "-----------------------------------------".
           MOVE TOTAL-CHG TO FORM-VAL.
           DISPLAY "GROSS TOTAL:     " FORM-VAL.
           MOVE INSUR-COVER TO FORM-VAL.
           DISPLAY "Insurance Pays: -" FORM-VAL.
           DISPLAY "=========================================".
           MOVE PATIENT-OWES TO FORM-VAL.
           DISPLAY "PATIENT TO PAY:  " FORM-VAL.
           DISPLAY "=========================================".
