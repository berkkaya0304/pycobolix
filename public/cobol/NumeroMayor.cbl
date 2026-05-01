      
       IDENTIFICATION DIVISION.
        PROGRAM-ID. Programa1.
        AUTHOR. Carlos García.
        
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        
        77 Num-Mayor PIC 99 VALUE 0.
        77 Num-Teclado PIC 99.
        77 Contador PIC 99 VALUE 0.
        
        PROCEDURE DIVISION.
        
        LogicaPrincipal.
            PERFORM LeerPrimerNumero.
            PERFORM LeerNumeros UNTIL Contador >= 10.
            DISPLAY "El mayor de los diez es: " Num-Mayor.
            STOP RUN.

        LeerPrimerNumero.
            DISPLAY "Introduce diez números y te digo cual es el mayor".
            DISPLAY "Introduce el primer número".
            ACCEPT Num-Mayor.
            ADD 1 TO Contador.
            
        LeerNumeros.
            DISPLAY "Introduce otro número".
            ACCEPT Num-Teclado.
            IF Num-Teclado > Num-Mayor
            THEN MOVE Num-Teclado TO Num-Mayor.
            ADD 1 TO Contador.
            
