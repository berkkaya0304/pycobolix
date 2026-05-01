       IDENTIFICATION DIVISION.
       PROGRAM-ID. PET-CLINIC.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PATIENT-INFO.
          05 PET-NAME        PIC X(20).
          05 PET-TYPE        PIC X(10).
          05 OWNER-NAME      PIC X(25).

       01 VET-SERVICES.
          05 CONSULT-FEE     PIC 9(3)V99 VALUE 65.00.
          05 VACCINE-QTY     PIC 9.
          05 VACCINE-FEE     PIC 9(3)V99 VALUE ZERO.
          05 BLOOD-TEST      PIC X.
          05 TEST-FEE        PIC 9(3)V99 VALUE ZERO.
          05 MEDICATION-AMT  PIC 9(3)V99 VALUE ZERO.

       01 BILLING.
          05 SUB-TOTAL       PIC 9(4)V99.
          05 TAX             PIC 9(3)V99.
          05 GRAND-TOTAL     PIC 9(5)V99.

       01 FMT-C             PIC $ZZ,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-PGM.
           DISPLAY "=== PAWS & CLAWS VET CLINIC ===".
           DISPLAY "Pet Name: ".
           ACCEPT PET-NAME.
           DISPLAY "Pet Type (Dog/Cat/Bird/etc): ".
           ACCEPT PET-TYPE.
           DISPLAY "Owner Name: ".
           ACCEPT OWNER-NAME.

           DISPLAY "Number of Vaccines given ($25 each): ".
           ACCEPT VACCINE-QTY.
           DISPLAY "Perform Blood Work? ($100) (Y/N): ".
           ACCEPT BLOOD-TEST.
           DISPLAY "Cost of Dispensed Medications ($): ".
           ACCEPT MEDICATION-AMT.

           PERFORM CALC-BILL.
           PERFORM PRINT-BILL.
           STOP RUN.

       CALC-BILL.
           COMPUTE VACCINE-FEE = VACCINE-QTY * 25.00.
           
           IF BLOOD-TEST = 'Y' OR 'y'
               MOVE 100.00 TO TEST-FEE
           END-IF.

           COMPUTE SUB-TOTAL = CONSULT-FEE + VACCINE-FEE 
                             + TEST-FEE + MEDICATION-AMT.
           COMPUTE TAX = SUB-TOTAL * 0.05.
           COMPUTE GRAND-TOTAL = SUB-TOTAL + TAX.

       PRINT-BILL.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "           CLINIC INVOICE                "
           DISPLAY "========================================="
           DISPLAY "Patient: " PET-NAME " (" PET-TYPE ")"
           DISPLAY "Owner:   " OWNER-NAME
           DISPLAY "-----------------------------------------"
           MOVE CONSULT-FEE TO FMT-C.
           DISPLAY "General Consultation: " FMT-C.
           IF VACCINE-FEE > 0
               MOVE VACCINE-FEE TO FMT-C
               DISPLAY "Vaccinations (" VACCINE-QTY "):    " FMT-C
           END-IF.
           IF TEST-FEE > 0
               MOVE TEST-FEE TO FMT-C
               DISPLAY "Laboratory/Blood:     " FMT-C
           END-IF.
           IF MEDICATION-AMT > 0
               MOVE MEDICATION-AMT TO FMT-C
               DISPLAY "Prescription Meds:    " FMT-C
           END-IF.
           DISPLAY "-----------------------------------------"
           MOVE SUB-TOTAL TO FMT-C.
           DISPLAY "SubTotal:             " FMT-C.
           MOVE TAX TO FMT-C.
           DISPLAY "Tax (5%):             " FMT-C.
           DISPLAY "========================================="
           MOVE GRAND-TOTAL TO FMT-C.
           DISPLAY "TOTAL BALANCE DUE:    " FMT-C.
           DISPLAY "=========================================".
