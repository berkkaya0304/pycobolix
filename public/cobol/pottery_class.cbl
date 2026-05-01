       IDENTIFICATION DIVISION.
       PROGRAM-ID. POTTERY-CLASS.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CLASS-RES.
          05 STUDENT-NAME    PIC X(20).
          05 CLAY-LBS        PIC 9(2)V9.
          05 TICKET-TYPE     PIC 9.
             88 DROP-IN      VALUE 1.
             88 MEMBER       VALUE 2.
          05 KILN-FIRING     PIC 9(2).

       01 COSTS.
          05 STUDIO-FEE      PIC 9(2)V99 VALUE ZERO.
          05 CLAY-FEE        PIC 9(2)V99 VALUE ZERO.
          05 KILN-FEE        PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-STUDIO.
           DISPLAY "--- CLAY CREATIONS STUDIO ---".
           DISPLAY "Student Name: ".
           ACCEPT STUDENT-NAME.
           DISPLAY "Session (1=Drop-In $35, 2=Member $0): ".
           ACCEPT TICKET-TYPE.
           DISPLAY "Clay Required (Lbs, $2.50/lb): ".
           ACCEPT CLAY-LBS.
           DISPLAY "Items to Kiln Fire/Glaze ($5.00 ea): ".
           ACCEPT KILN-FIRING.

           EVALUATE TRUE
               WHEN DROP-IN
                   MOVE 35.00 TO STUDIO-FEE
               WHEN MEMBER
                   MOVE ZERO TO STUDIO-FEE
               WHEN OTHER
                   MOVE 35.00 TO STUDIO-FEE
           END-EVALUATE.

           COMPUTE CLAY-FEE = CLAY-LBS * 2.50.
           COMPUTE KILN-FEE = KILN-FIRING * 5.00.

           COMPUTE GRAND-TOT = STUDIO-FEE + CLAY-FEE + KILN-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            STUDIO WORKSHOP             "
           DISPLAY "========================================"
           DISPLAY "Maker: " STUDENT-NAME
           DISPLAY "----------------------------------------"
           MOVE STUDIO-FEE TO DISP.
           DISPLAY "Studio Access Fee:  " DISP.
           
           IF CLAY-LBS > 0
               MOVE CLAY-FEE TO DISP
               DISPLAY "Clay (" CLAY-LBS " lbs):      " DISP
           END-IF.
           
           IF KILN-FIRING > 0
               MOVE KILN-FEE TO DISP
               DISPLAY "Kiln Firing (" KILN-FIRING "):   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL COST:         " DISP.
           DISPLAY "========================================".
           STOP RUN.
