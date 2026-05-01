       IDENTIFICATION DIVISION.
       PROGRAM-ID. BOWLING-ALLEY.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PARTY-INFO.
          05 PARTY-NAME      PIC X(20).
          05 NUMBER-PLAYERS  PIC 9(2).
          05 GAMES-PLAYED    PIC 9(2).
          05 SHOE-RENTALS    PIC 9(2).
          05 LEAGUE-MEMBER   PIC X.
             88 IS-LEAGUE    VALUE 'Y'.

       01 RATES-AND-FEES.
          05 RATE-PER-GAME   PIC 9(2)V99 VALUE 6.00.
          05 SHOE-FEE        PIC 9(2)V99 VALUE 4.00.
          05 TOTAL-GAMES     PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-SHOES     PIC 9(3)V99 VALUE ZERO.
          05 GROSS-AMT       PIC 9(4)V99 VALUE ZERO.
          05 LEAGUE-DISC     PIC 9(3)V99 VALUE ZERO.
          05 NET-AMT         PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       APP-START.
           DISPLAY "--- STRIKE ZONE BOWLING ---".
           DISPLAY "Party Name: ".
           ACCEPT PARTY-NAME.
           DISPLAY "Number of Players: ".
           ACCEPT NUMBER-PLAYERS.
           DISPLAY "Number of Games Bowled: ".
           ACCEPT GAMES-PLAYED.
           DISPLAY "Number of Shoe Rentals ($4 each): ".
           ACCEPT SHOE-RENTALS.
           DISPLAY "League Member? (15% discount) (Y/N): ".
           ACCEPT LEAGUE-MEMBER.

           COMPUTE TOTAL-GAMES = NUMBER-PLAYERS * GAMES-PLAYED 
                               * RATE-PER-GAME.
           COMPUTE TOTAL-SHOES = SHOE-RENTALS * SHOE-FEE.

           COMPUTE GROSS-AMT = TOTAL-GAMES + TOTAL-SHOES.

           IF IS-LEAGUE
               COMPUTE LEAGUE-DISC = GROSS-AMT * 0.15
           END-IF.

           COMPUTE NET-AMT = GROSS-AMT - LEAGUE-DISC.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             LANE RECEIPT               "
           DISPLAY "========================================"
           DISPLAY "Party: " PARTY-NAME
           DISPLAY "Players: " NUMBER-PLAYERS " | Games: " GAMES-PLAYED
           DISPLAY "----------------------------------------"
           MOVE TOTAL-GAMES TO DISP.
           DISPLAY "Games Total:        " DISP.
           
           IF TOTAL-SHOES > 0
               MOVE TOTAL-SHOES TO DISP
               DISPLAY "Shoe Rentals (" SHOE-RENTALS "):  " DISP
           END-IF.
           
           IF IS-LEAGUE
               MOVE LEAGUE-DISC TO DISP
               DISPLAY "League Discount:   -" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE NET-AMT TO DISP.
           DISPLAY "TOTAL LANE FEE:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
