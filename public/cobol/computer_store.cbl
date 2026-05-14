       IDENTIFICATION DIVISION.
       PROGRAM-ID. COMPUTER-STORE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PC-PARTS.
          05 CPU-CHOICE      PIC 9.
             88 I5-PROC      VALUE 1.
             88 I7-PROC      VALUE 2.
             88 I9-PROC      VALUE 3.
          05 RAM-CHOICE      PIC 9.
             88 RAM-16GB     VALUE 1.
             88 RAM-32GB     VALUE 2.
          05 GPU-CHOICE      PIC 9.
             88 GPU-RTX4060  VALUE 1.
             88 GPU-RTX4080  VALUE 2.

       01 PRICES.
          05 CPU-PRC         PIC 9(4)V99 VALUE ZERO.
          05 RAM-PRC         PIC 9(3)V99 VALUE ZERO.
          05 GPU-PRC         PIC 9(4)V99 VALUE ZERO.
          05 BUILD-FEE       PIC 9(3)V99 VALUE 99.00.
          05 TOTAL-SYS       PIC 9(5)V99 VALUE ZERO.

       01 DISP-FMT           PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       BUILD-PC.
           DISPLAY "--- CUSTOM PC BUILDER ---".
           DISPLAY "Select CPU: 1=i5($200), 2=i7($350), 3=i9($550): ".
           ACCEPT CPU-CHOICE.
           DISPLAY "Select RAM: 1=16GB($80), 2=32GB($150): ".
           ACCEPT RAM-CHOICE.
           DISPLAY "Select GPU: 1=RTX4060($300), 2=RTX4080($900): ".
           ACCEPT GPU-CHOICE.

           PERFORM CALC-SYSTEM.
           PERFORM PRINT-QUOTE.
           STOP RUN.

       CALC-SYSTEM.
           EVALUATE TRUE
               WHEN I5-PROC
                   MOVE 200.00 TO CPU-PRC
               WHEN I7-PROC
                   MOVE 350.00 TO CPU-PRC
               WHEN I9-PROC
                   MOVE 550.00 TO CPU-PRC
               WHEN OTHER
                   MOVE 200.00 TO CPU-PRC
           END-EVALUATE.

           EVALUATE TRUE
               WHEN RAM-16GB
                   MOVE 80.00 TO RAM-PRC
               WHEN RAM-32GB
                   MOVE 150.00 TO RAM-PRC
               WHEN OTHER
                   MOVE 80.00 TO RAM-PRC
           END-EVALUATE.

           EVALUATE TRUE
               WHEN GPU-RTX4060
                   MOVE 300.00 TO GPU-PRC
               WHEN GPU-RTX4080
                   MOVE 900.00 TO GPU-PRC
               WHEN OTHER
                   MOVE 300.00 TO GPU-PRC
           END-EVALUATE.

           COMPUTE TOTAL-SYS = CPU-PRC + RAM-PRC + GPU-PRC + BUILD-FEE.

       PRINT-QUOTE.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           PC BUILD QUOTE               "
           DISPLAY "========================================"
           MOVE CPU-PRC TO DISP-FMT. DISPLAY "Processor:   " DISP-FMT.
           MOVE RAM-PRC TO DISP-FMT. DISPLAY "Memory:      " DISP-FMT.
           MOVE GPU-PRC TO DISP-FMT. DISPLAY "Graphics:    " DISP-FMT.
           DISPLAY "----------------------------------------"
           MOVE BUILD-FEE TO DISP-FMT. DISPLAY "Assembly Fee:" DISP-FMT.
           MOVE TOTAL-SYS TO DISP-FMT.
           DISPLAY "----------------------------------------"
           DISPLAY "TOTAL SYSTEM COST: " DISP-FMT.
           DISPLAY "=======================================".
