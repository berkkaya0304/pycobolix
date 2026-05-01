           IDENTIFICATION DIVISION.
           PROGRAM-ID. KG_TO_POUNDS.
           AUTHOR. FILIP JANJESIC.
           DATA DIVISION.
           WORKING-STORAGE SECTION.
                01 WS-KG PIC 9(5)V99.
                01 WS-POUNDS PIC 9(5)V99.
                01 WS-DISPLAY-POUNDS PIC Z(5).99.
                01 WS-CONVERSION-FACTOR CONSTANT 2.20462.

           PROCEDURE DIVISION.
                DISPLAY "Enter weight in kilograms: ".
                ACCEPT WS-KG.
                MULTIPLY WS-KG BY WS-CONVERSION-FACTOR GIVING WS-POUNDS.
                MOVE WS-POUNDS TO WS-DISPLAY-POUNDS.
                DISPLAY "Weight in pounds: " WS-DISPLAY-POUNDS.
       
                STOP RUN.
           END PROGRAM KG_TO_POUNDS.
