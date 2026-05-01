       IDENTIFICATION DIVISION.
       PROGRAM-ID. SHIPPING-COST.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PACKAGE-INFO.
          05 SENDER-NAME     PIC X(20).
          05 WEIGHT-KG       PIC 9(3)V99.
          05 DIM-LENGTH      PIC 9(3).
          05 DIM-WIDTH       PIC 9(3).
          05 DIM-HEIGHT      PIC 9(3).
          05 ZONE-CODE       PIC 9.
             88 LOCAL-ZONE   VALUE 1.
             88 REGIONAL     VALUE 2.
             88 NATIONAL     VALUE 3.

       01 COMPUTED-VALS.
          05 VOLUMETRIC-WT   PIC 9(4)V99.
          05 CHARGEABLE-WT   PIC 9(4)V99.
          05 ZONE-MULTIPLIER PIC 9V99.
          05 BASE-SHIPPING   PIC 9(4)V99.
          
       01 DISP-FMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-APP.
           DISPLAY "--- GLOBAL COURIER LOGISTICS ---".
           DISPLAY "Sender Name: ".
           ACCEPT SENDER-NAME.
           DISPLAY "Package Weight (kg): ".
           ACCEPT WEIGHT-KG.
           DISPLAY "Length (cm): ".
           ACCEPT DIM-LENGTH.
           DISPLAY "Width (cm): ".
           ACCEPT DIM-WIDTH.
           DISPLAY "Height (cm): ".
           ACCEPT DIM-HEIGHT.
           DISPLAY "Zone (1=Local, 2=Regional, 3=National): ".
           ACCEPT ZONE-CODE.

           PERFORM DETERMINE-COST.
           PERFORM PRINT-LABEL.
           STOP RUN.

       DETERMINE-COST.
           COMPUTE VOLUMETRIC-WT = (DIM-LENGTH * DIM-WIDTH * DIM-HEIGHT) / 5000.
           
           IF VOLUMETRIC-WT > WEIGHT-KG
               MOVE VOLUMETRIC-WT TO CHARGEABLE-WT
           ELSE
               MOVE WEIGHT-KG TO CHARGEABLE-WT
           END-IF.

           EVALUATE TRUE
               WHEN LOCAL-ZONE
                   MOVE 1.25 TO ZONE-MULTIPLIER
               WHEN REGIONAL
                   MOVE 2.50 TO ZONE-MULTIPLIER
               WHEN NATIONAL
                   MOVE 4.00 TO ZONE-MULTIPLIER
               WHEN OTHER
                   MOVE 4.00 TO ZONE-MULTIPLIER
                   DISPLAY "Unknown zone. Defaulting to National."
           END-EVALUATE.

           COMPUTE BASE-SHIPPING = CHARGEABLE-WT * ZONE-MULTIPLIER.
           
           ADD 5.00 TO BASE-SHIPPING.

       PRINT-LABEL.
           DISPLAY " "
           DISPLAY "===================================="
           DISPLAY "         SHIPPING MANIFEST          "
           DISPLAY "===================================="
           DISPLAY "Sender: " SENDER-NAME.
           DISPLAY "Zone:   " ZONE-CODE.
           DISPLAY "------------------------------------"
           DISPLAY "Actual Weight:     " WEIGHT-KG " kg"
           DISPLAY "Volumetric Weight: " VOLUMETRIC-WT " kg"
           DISPLAY "Chargeable Weight: " CHARGEABLE-WT " kg"
           DISPLAY "------------------------------------"
           MOVE BASE-SHIPPING TO DISP-FMT.
           DISPLAY "TOTAL POSTAGE:     " DISP-FMT.
           DISPLAY "====================================".
