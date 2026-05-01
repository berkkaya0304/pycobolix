       IDENTIFICATION DIVISION.
       PROGRAM-ID. MUSEUM-ENTRY.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TICKET-REQUEST.
          05 GENERAL-QTY     PIC 9(2) VALUE ZERO.
          05 STUDENT-QTY     PIC 9(2) VALUE ZERO.
          05 SENIOR-QTY      PIC 9(2) VALUE ZERO.
          
       01 ADD-ONS.
          05 AUDIO-GUIDES    PIC 9(2) VALUE ZERO.
          05 SPEC-EXHIBIT    PIC 9(2) VALUE ZERO.
          
       01 COSTS.
          05 GEN-RATE        PIC 9(2)V99 VALUE 25.00.
          05 STU-RATE        PIC 9(2)V99 VALUE 15.00.
          05 SEN-RATE        PIC 9(2)V99 VALUE 12.00.
          05 AUDIO-RATE      PIC 9(2)V99 VALUE 8.00.
          05 SPEC-RATE       PIC 9(2)V99 VALUE 10.00.
          
          05 TOTAL-COST      PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- NATIONAL HISTORY MUSEUM ---".
           DISPLAY "General Admission QTY ($25): ".
           ACCEPT GENERAL-QTY.
           DISPLAY "Student Admission QTY ($15): ".
           ACCEPT STUDENT-QTY.
           DISPLAY "Senior Admission QTY ($12): ".
           ACCEPT SENIOR-QTY.
           
           DISPLAY "Audio Guides ($8 each): ".
           ACCEPT AUDIO-GUIDES.
           DISPLAY "Special Exhibit Passes ($10 each): ".
           ACCEPT SPEC-EXHIBIT.

           COMPUTE TOTAL-COST = (GENERAL-QTY * GEN-RATE)
                              + (STUDENT-QTY * STU-RATE)
                              + (SENIOR-QTY * SEN-RATE)
                              + (AUDIO-GUIDES * AUDIO-RATE)
                              + (SPEC-EXHIBIT * SPEC-RATE).

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          MUSEUM TICKET RECIEPT         "
           DISPLAY "========================================"
           IF GENERAL-QTY > 0
               COMPUTE DISP = GENERAL-QTY * GEN-RATE
               DISPLAY GENERAL-QTY "x General Adm:    " DISP
           END-IF.
           IF STUDENT-QTY > 0
               COMPUTE DISP = STUDENT-QTY * STU-RATE
               DISPLAY STUDENT-QTY "x Student Adm:    " DISP
           END-IF.
           IF SENIOR-QTY > 0
               COMPUTE DISP = SENIOR-QTY * SEN-RATE
               DISPLAY SENIOR-QTY "x Senior Adm:     " DISP
           END-IF.
           IF AUDIO-GUIDES > 0
               COMPUTE DISP = AUDIO-GUIDES * AUDIO-RATE
               DISPLAY AUDIO-GUIDES "x Audio Guides:   " DISP
           END-IF.
           IF SPEC-EXHIBIT > 0
               COMPUTE DISP = SPEC-EXHIBIT * SPEC-RATE
               DISPLAY SPEC-EXHIBIT "x Spec. Exhibit:  " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-COST TO DISP.
           DISPLAY "TOTAL ADMISSION:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
