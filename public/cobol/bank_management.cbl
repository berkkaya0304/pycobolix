       IDENTIFICATION DIVISION.
       PROGRAM-ID. BANK-MANAGEMENT.
       AUTHOR. ANTIGRAVITY.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ACCOUNT-INFO.
          05 ACC-NUMBER      PIC 9(10).
          05 ACC-HOLDER      PIC X(25).
          05 BALANCE         PIC 9(7)V99 VALUE ZERO.
          
       01 TRANSACTION-INFO.
          05 TRANS-TYPE      PIC X.
          05 TRANS-AMOUNT    PIC 9(7)V99.
          
       01 DISPLAY-VALUES.
          05 DISP-BALANCE    PIC $Z,ZZZ,ZZZ,ZZ9.99.
          05 USER-CHOICE     PIC X VALUE 'Y'.
          
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           DISPLAY "Welcome to Simple Bank System".
           DISPLAY "Enter Account Number (10 digits): ".
           ACCEPT ACC-NUMBER.
           DISPLAY "Enter Account Holder Name: ".
           ACCEPT ACC-HOLDER.
           DISPLAY "Enter Initial Deposit Amount: ".
           ACCEPT BALANCE.
           
           PERFORM PROCESS-TRANSACTIONS UNTIL USER-CHOICE = '4'.
           
           DISPLAY "Thank you for using our bank, " ACC-HOLDER ".".
           DISPLAY "Final Balance: " DISP-BALANCE.
           STOP RUN.

       PROCESS-TRANSACTIONS.
           DISPLAY " ".
           DISPLAY "--- MAIN MENU ---".
           DISPLAY "1. Check Balance".
           DISPLAY "2. Deposit Funds".
           DISPLAY "3. Withdraw Funds".
           DISPLAY "4. Exit".
           DISPLAY "Enter Your Choice (1-4): ".
           ACCEPT USER-CHOICE.
           
           EVALUATE USER-CHOICE
               WHEN '1'
                   PERFORM SHOW-BALANCE
               WHEN '2'
                   PERFORM MAKE-DEPOSIT
               WHEN '3'
                   PERFORM MAKE-WITHDRAWAL
               WHEN '4'
                   CONTINUE
               WHEN OTHER
                   DISPLAY "Invalid Choice. Try again."
           END-EVALUATE.
           
       SHOW-BALANCE.
           MOVE BALANCE TO DISP-BALANCE.
           DISPLAY "----------------------------------".
           DISPLAY "Current Balance for " ACC-NUMBER " is " DISP-BALANCE.
           DISPLAY "----------------------------------".

       MAKE-DEPOSIT.
           DISPLAY "Enter amount to deposit: ".
           ACCEPT TRANS-AMOUNT.
           ADD TRANS-AMOUNT TO BALANCE.
           DISPLAY "Deposit successful.".
           PERFORM SHOW-BALANCE.

       MAKE-WITHDRAWAL.
           DISPLAY "Enter amount to withdraw: ".
           ACCEPT TRANS-AMOUNT.
           IF TRANS-AMOUNT > BALANCE
               DISPLAY "Error: Insufficient Funds!"
               DISPLAY "Failed to withdraw."
           ELSE
               SUBTRACT TRANS-AMOUNT FROM BALANCE
               DISPLAY "Withdrawal successful."
               PERFORM SHOW-BALANCE
           END-IF.
