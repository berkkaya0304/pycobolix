       IDENTIFICATION DIVISION.
       PROGRAM-ID. GYM-MEMBERSHIP.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MEMBER-INPUT.
          05 M-NAME          PIC X(25).
          05 PLAN-TYPE       PIC X.
             88 P-MONTHLY    VALUE 'M'.
             88 P-YEARLY     VALUE 'Y'.
          05 TRAINER-REQ     PIC X.
             88 WANTS-PT     VALUE 'Y'.

       01 FEES.
          05 INIT-FEE        PIC 9(3)V99 VALUE 50.00.
          05 BASE-PLAN       PIC 9(4)V99 VALUE ZERO.
          05 PT-FEE          PIC 9(4)V99 VALUE ZERO.
          05 DISCOUNTS       PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-PAY       PIC 9(5)V99 VALUE ZERO.

       01 DISPLAY-VAL        PIC $Z,ZZ9.99.
       01 RUN-LOOP           PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       START-GYM.
           DISPLAY "*** IRON FIT STUDIO REGISTRATION ***".
           PERFORM UNTIL RUN-LOOP = 'N' OR 'n'
               PERFORM GET-MEMBER
               PERFORM CALC-FEES
               PERFORM SHOW-CONTRACT
               DISPLAY "Register another member? (Y/N): "
               ACCEPT RUN-LOOP
           END-PERFORM.
           STOP RUN.

       GET-MEMBER.
           DISPLAY "Enter New Member Name: ".
           ACCEPT M-NAME.
           DISPLAY "Plan Type (M=Monthly $40, Y=Yearly $400): ".
           ACCEPT PLAN-TYPE.
           DISPLAY "Add Personal Trainer (+$100/mo or $1000/yr)? (Y/N): ".
           ACCEPT TRAINER-REQ.

       CALC-FEES.
           MOVE ZERO TO DISCOUNTS.
           MOVE ZERO TO PT-FEE.
           MOVE 50.00 TO INIT-FEE.
           
           EVALUATE TRUE
               WHEN P-MONTHLY
                   MOVE 40.00 TO BASE-PLAN
                   IF WANTS-PT
                       MOVE 100.00 TO PT-FEE
                   END-IF
               WHEN P-YEARLY
                   MOVE 400.00 TO BASE-PLAN
                   COMPUTE DISCOUNTS = 50.00
                   IF WANTS-PT
                       MOVE 1000.00 TO PT-FEE
                   END-IF
               WHEN OTHER
                   MOVE 40.00 TO BASE-PLAN
                   DISPLAY "Invalid plan, defaulting to Monthly."
           END-EVALUATE.

           COMPUTE TOTAL-PAY = INIT-FEE + BASE-PLAN + PT-FEE - DISCOUNTS.

       SHOW-CONTRACT.
           DISPLAY " "
           DISPLAY "======================================"
           DISPLAY "      MEMBERSHIP AGREEMENT            "
           DISPLAY "======================================"
           DISPLAY "Member: " M-NAME.
           
           MOVE INIT-FEE TO DISPLAY-VAL.
           DISPLAY "Initiation Fee:  " DISPLAY-VAL.
           
           IF DISCOUNTS > 0
               MOVE DISCOUNTS TO DISPLAY-VAL
               DISPLAY "Promo Discount:  -" DISPLAY-VAL
           END-IF.
           
           MOVE BASE-PLAN TO DISPLAY-VAL.
           DISPLAY "Plan Fee:        " DISPLAY-VAL.
           
           IF PT-FEE > 0
               MOVE PT-FEE TO DISPLAY-VAL
               DISPLAY "Trainer Fee:     " DISPLAY-VAL
           END-IF.
           
           DISPLAY "--------------------------------------".
           MOVE TOTAL-PAY TO DISPLAY-VAL.
           DISPLAY "DUE TODAY:       " DISPLAY-VAL.
           DISPLAY "======================================".
