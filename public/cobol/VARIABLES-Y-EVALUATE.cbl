      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VARIABLES-Y-EVALUATE.
      ******************************************************************
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      ******************************************************************
      *                       VARIABLES                                *
      ******************************************************************
       01 WK-USUARIO.
           02 WK-ALUMNO.
               05 WK-NOMBRE-ALUMNO           PIC X(8)    VALUE SPACES.
               05 WK-APELLIDOS-ALUMNO.
                   10 WK-APELLIDO1-ALUMNO    PIC X(10)   VALUE SPACES.
                   10 WK-APELLIDO2-ALUMNO    PIC X(10)   VALUE SPACES.
               05 WK-TELEFONOS-ALUMNO.
                   10 WK-TELEFONO1-ALUMNO    PIC X(9)    VALUE SPACES.
                   10 WK-TELEFONO2-ALUMNO    PIC X(9)    VALUE SPACES.
           02 WK-PROFESOR.
               05 WK-NOMBRE-PROFESOR         PIC X(8)    VALUE SPACES.
               05 WK-APELLIDOS-PROFESOR.
                   10 WK-APELLIDO1-PROFESOR  PIC X(10)   VALUE SPACES.
                   10 WK-APELLIDO2-PROFESOR  PIC X(10)   VALUE SPACES.
               05 WK-TELEFONOS-PROFESOR.
                   10 WK-TELEFONO1-PROFESOR  PIC X(9)    VALUE SPACES.
                   10 WK-TELEFONO2-PROFESOR  PIC X(9)    VALUE SPACES.

       77 WK-OTRA-VARIABLE-INDEPENDIENTE     PIC 9(9)    VALUE ZEROES.

       01 WK-EDAD                            PIC 9(3)    VALUE ZEROES.
           88 WK-JOVEN                       VALUE 1     THRU 39.
           88 WK-MADURO                      VALUE 40    THRU 65.
           88 WK-ANCIANO                     VALUE 66    THRU 100.

       01 WK-COLORES                         PIC X(9)    VALUE SPACES.
           88 WK-PRIMARIOS         VALUES     "AMARILLO","AZUL", "ROJO".
           88 WK-SECUNDARIOS       VALUES "NARANJA", "VERDE", "VIOLETA".
           
      ******************************************************************
       PROCEDURE DIVISION.     
      *
           PERFORM 1000-INICIO
           PERFORM 2000-PROCESO
           PERFORM 3000-FIN
           .
      * 
      ******************************************************************
      *                       1000-INICIO                              *
      *----------------------------------------------------------------*
      *                                                                * 
      *                                                                *
      ****************************************************************** 
       1000-INICIO.
           
      ******************************************************************
      *                       2000-PROCESO                             *
      *----------------------------------------------------------------*
      *                                                                * 
      *                                                                *
      ****************************************************************** 
       2000-PROCESO.
      *
           PERFORM 2100-COMPRUEBA-EDAD
           PERFORM 2200-COMPRUEBA-EDAD-EVALUATE
           PERFORM 2300-COMPRUEBA-EVALUATE-TRUE
           PERFORM 2400-SELECCIONA-COLOR
           .
      *     
      ******************************************************************
      *                   2100-COMPRUEBA-EDAD                          *
      *----------------------------------------------------------------*
      *                                                                *
      ******************************************************************    
           2100-COMPRUEBA-EDAD.
      *
               DISPLAY 
               "INTRODUCE TU EDAD:"
               ACCEPT WK-EDAD

               IF WK-JOVEN 
                   THEN
                   DISPLAY 
                   "ERES JOVEN, " 
                   WITH NO ADVANCING
               END-IF

               IF WK-MADURO 
                   THEN
                   DISPLAY 
                   "ERES MADURO, " 
                   WITH NO ADVANCING
               END-IF

               IF WK-ANCIANO 
                   THEN
                   DISPLAY 
                   "ERES ANCIANO, " 
                   WITH NO ADVANCING
               END-IF

               DISPLAY 
               "TIENES " WK-EDAD " AÑOS."
               .
      *      
      ******************************************************************
      *                   2200-COMPRUEBA-EDAD-EVALUATE                 *
      *----------------------------------------------------------------*
      *                   MISMO CASO CON EVALUATE                      *
      ******************************************************************
           2200-COMPRUEBA-EDAD-EVALUATE.
      *
               DISPLAY 
               "INTRODUCE TU EDAD: "
               ACCEPT WK-EDAD    

   
               EVALUATE WK-EDAD

                    WHEN 1 THRU 39
                        DISPLAY 
                        "ERES JOVEN, TU EDAD ES " WK-EDAD "."

                    WHEN 40 THRU 65
                        DISPLAY 
                        "ERES MADURO, TU EDAD ES " WK-EDAD "."

                    WHEN 66 THRU 100
                        DISPLAY 
                        "ERES ANCIANO, TU EDAD ES " WK-EDAD "."

                    WHEN OTHER
                        DISPLAY 
                        "EDAD INCORRECTA."

               END-EVALUATE
               .
      *    
      ******************************************************************
      *                   2300-COMPRUEBA-EVALUATE-TRUE                 *
      *----------------------------------------------------------------*
      *              MISMO CASO CON EVALUATE TRUE,                     *
      *              DE ESTE MODO SE PUEDE USAR EL NIVEL 88            *
      ******************************************************************
           2300-COMPRUEBA-EVALUATE-TRUE.
      *
               DISPLAY "INTRODUCE TU EDAD: "
               ACCEPT WK-EDAD

                   EVALUATE TRUE

                   WHEN WK-JOVEN
                        DISPLAY
                        "ERES JOVEN, TU EDAD ES " WK-EDAD "."

                   WHEN WK-MADURO
                        DISPLAY 
                        "ERES MADURO, TU EDAD ES " WK-EDAD "."

                   WHEN WK-ANCIANO
                        DISPLAY 
                        "ERES ANCIANO, TU EDAD ES " WK-EDAD "."

                   WHEN OTHER
                        DISPLAY 
                        "EDAD INCORRECTA."

                   END-EVALUATE
                   .
      *         
      ******************************************************************
      *                   2400-SELECCIONA-COLOR                        *
      *----------------------------------------------------------------*
      *        COMPROBANDO VALORES CON EL "ARRAY" COLORES              *
      ******************************************************************    
           2400-SELECCIONA-COLOR.
      *
               DISPLAY 
               "INTRODUCE UN COLOR:"
               ACCEPT WK-COLORES
               
               IF WK-PRIMARIOS 
                   THEN
                   DISPLAY 
                   "ESE COLOR ES PRIMARIO."
               ELSE
               IF WK-SECUNDARIOS 
                   THEN
                   DISPLAY 
                   "ESE COLOR ES SECUNDARIO."
               ELSE
                   DISPLAY 
                   "NO TENGO ALMACENADO ESE COLOR."
               END-IF
               .
      *
      ******************************************************************
      *                   3000-FIN                                     *
      *----------------------------------------------------------------*
      *                                                                *
      ****************************************************************** 
       3000-FIN.
      *
            STOP RUN.
      *
      ******************************************************************


