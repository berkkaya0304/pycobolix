      
       IDENTIFICATION DIVISION.
        PROGRAM-ID. Programa2.
        AUTHOR. Carlos García.
        
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        
        01 Figura PIC X(9).
            88 Triangulo VALUE "triangulo", "TRIANGULO", "t", "T".
            88 Cuadrado VALUE "cuadrado", "CUADRADO", "c", "C".
            88 Pentagono VALUE "pentagono", "PENTAGONO", "p", "P".
            
        77 Base PIC 9(4).
        77 Altura PIC 9(4).
        77 Apotema PIC 9(4).
        77 Lado PIC 9(4).
        77 Area-Figura PIC 9(4) VALUE 0.
        
        PROCEDURE DIVISION.
        
        LogicaPrincipal.
        
            DISPLAY "Introduzca un nombre de figura" 
            " en minusculas y sin accentos".
            ACCEPT Figura.
        
              EVALUATE TRUE
                  WHEN Triangulo
                      PERFORM CalcAreaTriangulo
                  WHEN Cuadrado
                      PERFORM CalcAreaCuadrado
                  WHEN Pentagono
                      PERFORM CalcAreaPentagono
                  WHEN OTHER
                      DISPLAY "Figura no prevista"
              END-EVALUATE.
              
              PERFORM MostrarResultado.
              STOP RUN.
        
        MostrarResultado.
            IF Area-Figura NOT = 0 THEN 
            DISPLAY "El area es de: " Area-Figura " u^2".
        
        CalcAreaPentagono.
            DISPLAY "Introduce el apotema: ".
            ACCEPT Apotema.
            DISPLAY "Introduce el lado: ".
            ACCEPT Lado.
            
            MULTIPLY 5 BY Lado GIVING Area-Figura.
            MULTIPLY Area-Figura BY Apotema GIVING Area-Figura
            DIVIDE Area-Figura BY 2 GIVING Area-Figura.

        CalcAreaCuadrado.
            PERFORM PedirBaseAltura.
            COMPUTE Area-Figura = Base * Altura.
            
        CalcAreaTriangulo.
            PERFORM PedirBaseAltura.
            COMPUTE Area-Figura = Base * Altura / 2.
            
        PedirBaseAltura.
            DISPLAY "Introduce la base: ".
            ACCEPT Base.
            DISPLAY "Introduce la altura: ".
            ACCEPT Altura.
        
