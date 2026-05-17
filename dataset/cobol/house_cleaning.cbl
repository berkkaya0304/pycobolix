       IDENTIFICATION DIVISION.
       PROGRAM-ID. HOUSE-CLEANING.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 HOME-VARS.
          05 SQ-FOOTAGE      PIC 9(5).
          05 HAS-PETS        PIC X.
             88 PETS-YES     VALUE 'Y'.
          05 DEEP-CLEAN      PIC X.
             88 DC-YES       VALUE 'Y'.

       01 ESTIMATE-CALCS.
          05 BASE-RATE       PIC 9(3)V99 VALUE ZERO.
          05 PET-SURCHARGE   PIC 9(3)V99 VALUE ZERO.
          05 DC-SURCHARGE    PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-QUOTE     PIC 9(4)V99 VALUE ZERO.

       01 F-C                PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-QUOTE.
           DISPLAY "--- SPARKLE MAIDS QUOTE ---".
           DISPLAY "Approximate Sq Footage of house: ".
           ACCEPT SQ-FOOTAGE.
           DISPLAY "Do you have pets? (Y/N): ".
           ACCEPT HAS-PETS.
           DISPLAY "Require initial deep clean? (Y/N): ".
           ACCEPT DEEP-CLEAN.

           PERFORM DO-QUOTE.
           PERFORM SHOW-QUOTE.
           STOP RUN.

       DO-QUOTE.
           COMPUTE BASE-RATE = SQ-FOOTAGE * 0.10.

           IF PETS-YES
               MOVE 30.00 TO PET-SURCHARGE
           END-IF.

           IF DC-YES
               COMPUTE DC-SURCHARGE = BASE-RATE * 0.50
           END-IF.

           COMPUTE TOTAL-QUOTE = BASE-RATE + PET-SURCHARGE 
                               + DC-SURCHARGE.

       SHOW-QUOTE.
           DISPLAY " "
           DISPLAY "======================================"
           DISPLAY "        CLEANING SERVICE QUOTE        "
           DISPLAY "======================================"
           DISPLAY "Home Size: " SQ-FOOTAGE " sq ft."
           DISPLAY "--------------------------------------"
           MOVE BASE-RATE TO F-C.
           DISPLAY "Standard Cleaning Base: " F-C.
           
           IF PET-SURCHARGE > 0
               MOVE PET-SURCHARGE TO F-C
               DISPLAY "Pet Hair/Dander Fee:    " F-C
           END-IF.
           
           IF DC-SURCHARGE > 0
               MOVE DC-SURCHARGE TO F-C
               DISPLAY "Initial Deep Clean Add: " F-C
           END-IF.
           DISPLAY "--------------------------------------"
           MOVE TOTAL-QUOTE TO F-C.
           DISPLAY "ESTIMATED TOTAL:        " F-C.
           DISPLAY "======================================".
