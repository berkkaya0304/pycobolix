       IDENTIFICATION DIVISION.
       PROGRAM-ID. CAR-RENTAL-SYSTEM.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RENTAL-DATA.
          05 CUSTOMER-NAME   PIC X(25).
          05 CAR-CATEGORY    PIC 9.
          05 DAYS-RENTED     PIC 9(3).
          05 DRIVER-AGE      PIC 9(2).
          
       01 PRICING.
          05 BASE-RATE       PIC 9(3)V99 VALUE ZERO.
          05 AGE-SURCHARGE   PIC 9(3)V99 VALUE ZERO.
          05 INSUR-FEE       PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-COST      PIC 9(6)V99 VALUE ZERO.
          
       01 INSURANCE-FLAG     PIC X.
          88 WANTS-INSURANCE VALUE 'Y'.
          
       01 FM-COST            PIC $Z,ZZZ,ZZ9.99.
       01 IS-RUNNING         PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       MAIN-APP.
           DISPLAY "### RAPID RENTALS ###".
           PERFORM UNTIL IS-RUNNING = 'N' OR 'n'
               PERFORM GET-INPUTS
               PERFORM CALCULATIONS
               PERFORM PRINT-AGREEMENT
               DISPLAY "New rental? (Y/N): "
               ACCEPT IS-RUNNING
           END-PERFORM.
           STOP RUN.

       GET-INPUTS.
           DISPLAY "Customer Name: ".
           ACCEPT CUSTOMER-NAME.
           DISPLAY "Car Category (1=Eco $30, 2=Sedan $50, 3=SUV $80): ".
           ACCEPT CAR-CATEGORY.
           DISPLAY "Rental Duration (Days): ".
           ACCEPT DAYS-RENTED.
           DISPLAY "Driver's Age: ".
           ACCEPT DRIVER-AGE.
           DISPLAY "Add Full Insurance ($15/day)? (Y/N): ".
           ACCEPT INSURANCE-FLAG.

       CALCULATIONS.
           EVALUATE CAR-CATEGORY
               WHEN 1
                   MOVE 30.00 TO BASE-RATE
               WHEN 2
                   MOVE 50.00 TO BASE-RATE
               WHEN 3
                   MOVE 80.00 TO BASE-RATE
               WHEN OTHER
                   DISPLAY "Invalid category, assigning Eco."
                   MOVE 30.00 TO BASE-RATE
           END-EVALUATE.

           IF DRIVER-AGE < 25
               COMPUTE AGE-SURCHARGE = 20.00 * DAYS-RENTED
           ELSE
               MOVE ZERO TO AGE-SURCHARGE
           END-IF.

           IF WANTS-INSURANCE
               COMPUTE INSUR-FEE = 15.00 * DAYS-RENTED
           ELSE
               MOVE ZERO TO INSUR-FEE
           END-IF.

           COMPUTE TOTAL-COST = (BASE-RATE * DAYS-RENTED) 
                                + AGE-SURCHARGE + INSUR-FEE.

       PRINT-AGREEMENT.
           DISPLAY " "
           DISPLAY "=================================".
           DISPLAY " RENTAL AGREEMENT".
           DISPLAY "=================================".
           DISPLAY "Renter: " CUSTOMER-NAME.
           DISPLAY "Days:   " DAYS-RENTED.
           
           COMPUTE BASE-RATE = BASE-RATE * DAYS-RENTED.
           MOVE BASE-RATE TO FM-COST.
           DISPLAY "Base Rental:    " FM-COST.
           
           IF AGE-SURCHARGE > 0
               MOVE AGE-SURCHARGE TO FM-COST
               DISPLAY "Under 25 Fee:   " FM-COST
           END-IF.
           
           IF INSUR-FEE > 0
               MOVE INSUR-FEE TO FM-COST
               DISPLAY "Insurance Addon:" FM-COST
           END-IF.
           
           DISPLAY "---------------------------------".
           MOVE TOTAL-COST TO FM-COST.
           DISPLAY "TOTAL CHARGE:   " FM-COST.
           DISPLAY "=================================".
