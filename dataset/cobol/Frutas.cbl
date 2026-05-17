      
       IDENTIFICATION DIVISION.
        PROGRAM-ID. Programa3.
        AUTHOR. Carlos García.
        
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        
        77 Tabla-Frutas PIC X(12) OCCURS 10.
        
        77 Indice PIC 99 VALUE 1.
        77 Fruta-Tecleada PIC X(12).
        
        01 Continuar-Si-No PIC X.
            88 Opt-Si VALUE "S", "s".
            88  Opt-No VALUE "N", "n".
        
        PROCEDURE DIVISION.
        
        LogicaPrincipal.
            PERFORM IntroducirFrutas 
            UNTIL Indice > 10 OR Opt-No.
            PERFORM EvaluarResultado.
            STOP RUN.
        
        IntroducirFrutas.
            DISPLAY "Teclea el nombre de una fruta: ".
            ACCEPT Fruta-Tecleada.
            MOVE Fruta-Tecleada TO Tabla-Frutas(Indice).
            ADD 1 TO Indice.
            PERFORM ContinuarPregunta.
            
            
        ContinuarPregunta.
            DISPLAY "Deseas continuar? (S/N)". 
            ACCEPT Continuar-Si-No.
            
        EvaluarResultado.
            IF Indice > 10 THEN 
            DISPLAY "La tabla está llena."
            ELSE
            DISPLAY "Aún quedan elementos por rellenar.".
        
