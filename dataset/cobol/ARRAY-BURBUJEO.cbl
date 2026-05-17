      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. YOUR-PROGRAM-NAME.
      ******************************************************************
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      *
      ******************************************************************
      *                       VARIABLES                                *
      ******************************************************************
      *
       77 WK-AUX               PIC 9               VALUE ZERO.
       77 WK-INDICE-ARRAY      PIC 9               VALUE ZERO.
       77 WK-CONTADOR          PIC 9               VALUE ZERO.
       01 WS-ARRAY             OCCURS 5 TIMES      INDEXED BY IDX.
           05 WK-VALOR-ARRAY   PIC 9(1).
      *
      ******************************************************************
       PROCEDURE DIVISION.
      *
           PERFORM 1000-INCIO
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
       1000-INCIO.
      *
           MOVE 5  TO           WK-VALOR-ARRAY(1)
           MOVE 1  TO           WK-VALOR-ARRAY(2)
           MOVE 4  TO           WK-VALOR-ARRAY(3)
           MOVE 2  TO           WK-VALOR-ARRAY(4)
           MOVE 8  TO           WK-VALOR-ARRAY(5)
           .
      *
      ******************************************************************
      *                       2000-PROCESO                             *
      *----------------------------------------------------------------*
      *                                                                *
      *                                                                *
      ******************************************************************
       2000-PROCESO.
      *
           PERFORM 2100-MOSTRAR-ARRAY
           PERFORM 2200-ORDENAR-ARRAY
           PERFORM 2300-MOSTRAR-ARRAY-ORDENADO
           .
      *
      ******************************************************************
      *                       2100-MOSTRAR-ARRAY                       *
      *----------------------------------------------------------------*
      *                                                                *
      *                                                                *
      ******************************************************************
       2100-MOSTRAR-ARRAY.
      *
           DISPLAY
           "EL ARRAY ACTUAL ES: "
           PERFORM
           VARYING IDX FROM 1 BY 1
           UNTIL IDX > 5
           DISPLAY WK-VALOR-ARRAY(IDX) WITH NO ADVANCING
           IF IDX < 5
               DISPLAY
               ", " WITH NO ADVANCING
           ELSE
               DISPLAY
               " "
           END-PERFORM
           .
      *
      ******************************************************************
      *                       2200-ORDENAR-ARRAY                       *
      *----------------------------------------------------------------*
      *                                                                *
      *                                                                *
      ******************************************************************
       2200-ORDENAR-ARRAY.
      *
           MOVE 1 TO WK-INDICE-ARRAY
           PERFORM UNTIL WK-INDICE-ARRAY > 4
               MOVE 1 TO WK-CONTADOR
               PERFORM UNTIL WK-CONTADOR > 5 - WK-INDICE-ARRAY
                   IF WK-VALOR-ARRAY(WK-CONTADOR) >
                       WK-VALOR-ARRAY(WK-CONTADOR + 1)
                       MOVE WK-VALOR-ARRAY(WK-CONTADOR)
                       TO WK-AUX
                       MOVE WK-VALOR-ARRAY(WK-CONTADOR + 1)
                       TO WK-VALOR-ARRAY(WK-CONTADOR)
                       MOVE WK-AUX TO WK-VALOR-ARRAY(WK-CONTADOR + 1)
                   END-IF
                   ADD 1 TO WK-CONTADOR
               END-PERFORM
               ADD 1 TO WK-INDICE-ARRAY
           END-PERFORM
           .
      *
      ******************************************************************
      *     SI EL COMPLILADOR PERMITE IDX SE PODRÍA HACER ASÍ
      ******************************************************************
      *    PERFORM VARYING WK-INDICE-ARRAY FROM 1 BY 1
      *      UNTIL WK-INDICE-ARRAY > 4
      *      PERFORM VARYING IDX FROM 1 BY 1
      *          UNTIL IDX > 5 - WK-INDICE-ARRAY
      *          IF WK-VALOR-ARRAY(IDX) > WK-VALOR-ARRAY(IDX + 1)
      *              MOVE WK-VALOR-ARRAY(IDX) TO WK-AUX
      *              MOVE WK-VALOR-ARRAY(IDX + 1) TO WK-VALOR-ARRAY(IDX)
      *              MOVE WK-AUX TO WK-VALOR-ARRAY(IDX + 1)
      *          END-IF
      *      END-PERFORM
      *    END-PERFORM.
      ******************************************************************
      *
      ******************************************************************
      *                       2300-MOSTRAR-ARRAY-ORDENADO              *
      *----------------------------------------------------------------*
      *                                                                *
      *                                                                *
      ******************************************************************
       2300-MOSTRAR-ARRAY-ORDENADO.
      *
           DISPLAY
           "EL ARRAY ORDENADO ES: "
           PERFORM
           VARYING WK-INDICE-ARRAY FROM 1 BY 1
           UNTIL WK-INDICE-ARRAY > 5
           DISPLAY
           WK-VALOR-ARRAY(WK-INDICE-ARRAY) WITH NO ADVANCING
           IF WK-INDICE-ARRAY < 5
               DISPLAY
               ", " WITH NO ADVANCING
           END-PERFORM
           .
      *
      ******************************************************************
      *                       3000-FIN                                 *
      *----------------------------------------------------------------*
      *                                                                *
      *                                                                *
      ******************************************************************
       3000-FIN.
      *
           STOP RUN.
      ******************************************************************
