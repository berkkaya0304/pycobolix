       IDENTIFICATION DIVISION.
       PROGRAM-ID. RECORD-LABEL.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 STUDIO-INFO.
          05 ARTIST-NAME     PIC X(20).
          05 STUDIO-HOURS    PIC 9(2)V9.
          05 ENGINEER-REQ    PIC X.
             88 WANTS-ENG    VALUE 'Y'.
          05 MASTERING-TRK   PIC 9(2) VALUE ZERO.

       01 FEES.
          05 ROOM-RATE       PIC 9(2)V99 VALUE 50.00.
          05 ENG-RATE        PIC 9(2)V99 VALUE 40.00.
          05 MASTER-RATE     PIC 9(3)V99 VALUE 150.00.

       01 TOTS.
          05 ROOM-TOT        PIC 9(4)V99 VALUE ZERO.
          05 ENG-TOT         PIC 9(4)V99 VALUE ZERO.
          05 MASTER-TOT      PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-SESSION.
           DISPLAY "--- PLATINUM TRACKS STUDIO ---".
           DISPLAY "Artist / Band Name: ".
           ACCEPT ARTIST-NAME.
           DISPLAY "Studio Rental Duration (Hours): ".
           ACCEPT STUDIO-HOURS.
           DISPLAY "Require Sound Engineer ($40/hr)? (Y/N): ".
           ACCEPT ENGINEER-REQ.
           DISPLAY "Number of Tracks to Master ($150 ea): ".
           ACCEPT MASTERING-TRK.

           COMPUTE ROOM-TOT = STUDIO-HOURS * ROOM-RATE.

           IF WANTS-ENG
               COMPUTE ENG-TOT = STUDIO-HOURS * ENG-RATE
           END-IF.

           COMPUTE MASTER-TOT = MASTERING-TRK * MASTER-RATE.

           COMPUTE GRAND-TOT = ROOM-TOT + ENG-TOT + MASTER-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           STUDIO INVOICE               "
           DISPLAY "========================================"
           DISPLAY "Artist: " ARTIST-NAME
           DISPLAY "----------------------------------------"
           MOVE ROOM-TOT TO DISP.
           DISPLAY "Room Rental (" STUDIO-HOURS " hrs): " DISP.
           
           IF WANTS-ENG
               MOVE ENG-TOT TO DISP
               DISPLAY "Sound Engineer Fee:     " DISP
           END-IF.
           
           IF MASTERING-TRK > 0
               MOVE MASTER-TOT TO DISP
               DISPLAY "Audio Mastering (" MASTERING-TRK "):  " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL SESSION COST:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
