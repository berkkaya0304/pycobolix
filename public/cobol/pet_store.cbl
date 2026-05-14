       IDENTIFICATION DIVISION.
       PROGRAM-ID. PET-STORE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CART-DATA.
          05 FOOD-BAGS       PIC 9(2) VALUE ZERO.
          05 TOY-QTY         PIC 9(2) VALUE ZERO.
          05 GROOM-ITEMS     PIC 9(2) VALUE ZERO.
          05 VIP-MEMBER      PIC X.
             88 IS-VIP       VALUE 'Y'.

       01 PRICES.
          05 FOOD-PRICE      PIC 9(2)V99 VALUE 45.00.
          05 TOY-PRICE       PIC 9(2)V99 VALUE 12.50.
          05 GROOM-PRICE     PIC 9(2)V99 VALUE 18.00.

       01 BILLING.
          05 SUB-TOT         PIC 9(4)V99 VALUE ZERO.
          05 VIP-DISC        PIC 9(3)V99 VALUE ZERO.
          05 TAX-AMT         PIC 9(3)V99 VALUE ZERO.
          05 G-TOTAL         PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-STORE.
           DISPLAY "--- HAPPY PAWS PET EMPORIUM ---".
           DISPLAY "Dog/Cat Food Bags ($45 ea): ".
           ACCEPT FOOD-BAGS.
           DISPLAY "Pet Toys ($12.50 ea): ".
           ACCEPT TOY-QTY.
           DISPLAY "Grooming Supplies ($18 ea): ".
           ACCEPT GROOM-ITEMS.
           DISPLAY "VIP Rewards Member (15% off)? (Y/N): ".
           ACCEPT VIP-MEMBER.

           COMPUTE SUB-TOT = (FOOD-BAGS * FOOD-PRICE) 
                           + (TOY-QTY * TOY-PRICE) 
                           + (GROOM-ITEMS * GROOM-PRICE).

           IF IS-VIP
               COMPUTE VIP-DISC = SUB-TOT * 0.15
           END-IF.

           COMPUTE TAX-AMT = (SUB-TOT - VIP-DISC) * 0.08.

           COMPUTE G-TOTAL = SUB-TOT - VIP-DISC + TAX-AMT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            PET STORE RECEIPT           "
           DISPLAY "========================================"
           IF FOOD-BAGS > 0
               COMPUTE DISP = FOOD-BAGS * FOOD-PRICE
               DISPLAY FOOD-BAGS "x Pet Food:         " DISP
           END-IF.
           IF TOY-QTY > 0
               COMPUTE DISP = TOY-QTY * TOY-PRICE
               DISPLAY TOY-QTY "x Toys:             " DISP
           END-IF.
           IF GROOM-ITEMS > 0
               COMPUTE DISP = GROOM-ITEMS * GROOM-PRICE
               DISPLAY GROOM-ITEMS "x Grooming Items:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-TOT TO DISP.
           DISPLAY "Subtotal:            " DISP.
           IF IS-VIP
               MOVE VIP-DISC TO DISP
               DISPLAY "VIP Discount (15%): -" DISP
           END-IF.
           MOVE TAX-AMT TO DISP.
           DISPLAY "Sales Tax (8%):      " DISP.
           DISPLAY "----------------------------------------"
           MOVE G-TOTAL TO DISP.
           DISPLAY "TOTAL BALANCE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
