       IDENTIFICATION DIVISION.
       PROGRAM-ID. PHOTO-STUDIO.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SESSION-DATA.
          05 CLIENT-NAME     PIC X(20).
          05 SESSION-TYPE    PIC 9.
             88 STD-HEADSHOT VALUE 1.
             88 FAMILY-PORT  VALUE 2.
             88 EVENT-SHOOT  VALUE 3.
          05 PHY-PRINTS      PIC 9(2) VALUE ZERO.
          05 DIGITAL-COPY    PIC X.
             88 WANTS-DIGIT  VALUE 'Y'.

       01 FEES.
          05 SITTING-FEE     PIC 9(3)V99 VALUE ZERO.
          05 PRINT-FEE       PIC 9(3)V99 VALUE ZERO.
          05 DIGITAL-FEE     PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       STUDIO-START.
           DISPLAY "--- LENS APERTURE STUDIO ---".
           DISPLAY "Client: ".
           ACCEPT CLIENT-NAME.
           DISPLAY "Session (1=Headshot $99, 2=Family $150, 3=Event): ".
           ACCEPT SESSION-TYPE.
           DISPLAY "Physical Prints Wanted ($15 per sheet): ".
           ACCEPT PHY-PRINTS.
           DISPLAY "USB Drive with Digital Masters ($50)? (Y/N): ".
           ACCEPT DIGITAL-COPY.

           EVALUATE TRUE
               WHEN STD-HEADSHOT
                   MOVE 99.00 TO SITTING-FEE
               WHEN FAMILY-PORT
                   MOVE 150.00 TO SITTING-FEE
               WHEN EVENT-SHOOT
                   MOVE 300.00 TO SITTING-FEE
               WHEN OTHER
                   MOVE 99.00 TO SITTING-FEE
           END-EVALUATE.

           COMPUTE PRINT-FEE = PHY-PRINTS * 15.00.

           IF WANTS-DIGIT
               MOVE 50.00 TO DIGITAL-FEE
           END-IF.

           COMPUTE GRAND-TOTAL = SITTING-FEE + PRINT-FEE + DIGITAL-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          STUDIO INVOICE                "
           DISPLAY "========================================"
           DISPLAY "Client: " CLIENT-NAME
           DISPLAY "----------------------------------------"
           MOVE SITTING-FEE TO DISP.
           DISPLAY "Session/Sitting Fee: " DISP.
           
           IF PRINT-FEE > 0
               MOVE PRINT-FEE TO DISP
               DISPLAY "Physical Prints (" PHY-PRINTS "):  " DISP
           END-IF.
           
           IF DIGITAL-FEE > 0
               MOVE DIGITAL-FEE TO DISP
               DISPLAY "Digital Masters USB: " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOTAL TO DISP.
           DISPLAY "TOTAL CHARGED:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
