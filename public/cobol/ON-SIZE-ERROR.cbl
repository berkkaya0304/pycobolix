      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ON-SIZE-ERROR.
      ******************************************************************
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      *
      ******************************************************************
      *                       VARIABLES                                *
      ******************************************************************
      *
       77 WK-NUMERO1                  PIC 9(3)      VALUE 200.
       77 WK-NUMERO2                  PIC 9(3)      VALUE 100.
       77 WK-NUMERO3                  PIC 9(1)      VALUE 3.
       77 WK-NUMERO4                  PIC 9(1)      VALUE 4.
       77 WK-RESULTADO                PIC 9(3)      VALUE ZEROES.
       77 WK-RESULTADO-GRANDE         PIC 9(5)      VALUE ZEROES.
      *
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
           PERFORM 2100-PARRAFO
           PERFORM 2200-PARRAFO
           PERFORM 2300-PARRAFO
           PERFORM 2400-PARRAFO
           .
      *
      ******************************************************************
      *                   2100-                                        *
      *----------------------------------------------------------------*
      *                                                                *
      ******************************************************************
           2100-PARRAFO.
      *
           COMPUTE WK-RESULTADO = WK-NUMERO1 * WK-NUMERO2
                ON SIZE ERROR
                DISPLAY
                "NUMERO DEMASIADO GRANDE"
                DISPLAY WK-RESULTADO
           END-COMPUTE
           .
      *
      ******************************************************************
      *                   2200-                                        *
      *----------------------------------------------------------------*
      *                                                                *
      ******************************************************************
           2200-PARRAFO.
      *
           COMPUTE
           WK-RESULTADO = WK-NUMERO1 * WK-NUMERO2
               ON SIZE ERROR
               COMPUTE
               WK-RESULTADO-GRANDE = WK-NUMERO1 * WK-NUMERO2
                   DISPLAY
                   WK-RESULTADO-GRANDE
           END-COMPUTE
           .
      *
      ******************************************************************
      *                   2300-                                        *
      *----------------------------------------------------------------*
      *                                                                *
      ******************************************************************
           2300-PARRAFO.
      *
           COMPUTE
           WK-RESULTADO = WK-NUMERO1 * WK-NUMERO2
               ON SIZE ERROR
                   DISPLAY
                   "EL NUMERO ES MUY GRANDE, NO SE "-
                   "VISUALIZA ENTERO"
                   DISPLAY
                   "SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)"
                   MOVE 200                        TO WK-RESULTADO
                       NOT ON SIZE ERROR
                       DISPLAY WK-RESULTADO
           END-COMPUTE

           DISPLAY WK-RESULTADO
           .
      *
      ******************************************************************
      *                   2400-                                        *
      *----------------------------------------------------------------*
      *                                                                *
      ******************************************************************
           2400-PARRAFO.
      *
           COMPUTE
           WK-RESULTADO = WK-NUMERO3 * WK-NUMERO4
               ON SIZE ERROR
                   DISPLAY
                   "EL NUMERO ES MUY GRANDE, NO SE "-
                   "VISUALIZA ENTERO"
                   DISPLAY
                   "SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)"
                   MOVE 200                    TO WK-RESULTADO
                   NOT ON SIZE ERROR
                   DISPLAY WK-RESULTADO
           END-COMPUTE
           .
      *
      ******************************************************************
      *                   3000-FIN                                     *
      *----------------------------------------------------------------*
      *                                                                *
      ******************************************************************
       3000-FIN.
      *
            STOP RUN
            .
      *
      ******************************************************************


