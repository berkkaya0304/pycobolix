       IDENTIFICATION DIVISION.
       PROGRAM-ID. FIBONACCI.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 N            PIC 9(3).
       77 I            PIC 9(3).
       77 F1           PIC 9(9) VALUE 0.
       77 F2           PIC 9(9) VALUE 1.
       77 TEMP         PIC 9(9).

       PROCEDURE DIVISION.
       DISPLAY "Enter number of Fibonacci terms: ".
       ACCEPT N.

       DISPLAY "Fibonacci sequence using loop: ".
       PERFORM VARYING I FROM 1 BY 1 UNTIL I > N
           DISPLAY F1
           ADD F1 TO F2 GIVING TEMP
           MOVE F2 TO F1
           MOVE TEMP TO F2
       END-PERFORM.

       STOP RUN.
