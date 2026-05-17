       IDENTIFICATION DIVISION.
       PROGRAM-ID. ARCADE-CARD.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CARD-SETUP.
          05 PLAYER-TAG      PIC X(15).
          05 LOAD-AMOUNT     PIC 9(3)V99.
          05 IS-NEW-CARD     PIC X.
             88 NEW-CARD     VALUE 'Y'.
          05 VIP-STATUS      PIC X.
             88 IS-VIP       VALUE 'Y'.

       01 CREDITS.
          05 BASE-CR         PIC 9(5) VALUE ZERO.
          05 BONUS-CR        PIC 9(4) VALUE ZERO.
          05 VIP-CR          PIC 9(4) VALUE ZERO.
          05 TOTAL-CR        PIC 9(5) VALUE ZERO.
          05 FEES-PAID       PIC 9(3)V99 VALUE ZERO.

       01 DISP-F             PIC $Z,ZZ9.99.
       01 DISP-C             PIC ZZZ,ZZ9.

       PROCEDURE DIVISION.
       START-KIOSK.
           DISPLAY "--- GALAXY ARCADE KIOSK ---".
           DISPLAY "Player Tag / Nickname: ".
           ACCEPT PLAYER-TAG.
           DISPLAY "Amount to load ($): ".
           ACCEPT LOAD-AMOUNT.
           DISPLAY "Is this a new card issue ($2 fee)? (Y/N): ".
           ACCEPT IS-NEW-CARD.
           DISPLAY "Are you a VIP Gold Member? (Y/N): ".
           ACCEPT VIP-STATUS.

           COMPUTE BASE-CR = LOAD-AMOUNT * 4.

           IF LOAD-AMOUNT >= 50.00
               MOVE 50 TO BONUS-CR
           ELSE IF LOAD-AMOUNT >= 25.00
               MOVE 15 TO BONUS-CR
           ELSE
               MOVE ZERO TO BONUS-CR
           END-IF.

           IF IS-VIP
               COMPUTE VIP-CR = BASE-CR * 0.20
           END-IF.

           COMPUTE TOTAL-CR = BASE-CR + BONUS-CR + VIP-CR.

           IF NEW-CARD
               COMPUTE FEES-PAID = LOAD-AMOUNT + 2.00
           ELSE
               MOVE LOAD-AMOUNT TO FEES-PAID
           END-IF.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           CARD RELOAD RECIEPT          "
           DISPLAY "========================================"
           DISPLAY "Player: " PLAYER-TAG
           DISPLAY "----------------------------------------"
           MOVE LOAD-AMOUNT TO DISP-F.
           DISPLAY "Funds Loaded:       " DISP-F.
           IF NEW-CARD
               DISPLAY "New Card Fee:       $    2.00"
           END-IF.
           MOVE FEES-PAID TO DISP-F.
           DISPLAY "TOTAL CHARGED:      " DISP-F.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-CR TO DISP-C.
           DISPLAY "YOUR NEW ARCADE BALANCE:"
           DISPLAY "      " DISP-C " CREDITS"
           DISPLAY "========================================".
           STOP RUN.
