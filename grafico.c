#include <stdio.h>      // Incluye las funciones estándar de entrada y salida, como printf.
#include <stdlib.h>     // Incluye funciones generales como exit.
#include <graphics.h>   // Incluye funciones gráficas, como initgraph y line.

int main(void)
{
    int gd = DETECT, gm, errorcode;

    // Inicia el modo gráfico. 
    // 'gd' se establece en DETECT para que detecte automáticamente el driver de gráficos.
    // 'gm' es el modo gráfico que será determinado automáticamente.
    initgraph(&gd, &gm, "");

    // Verifica si la inicialización gráfica fue exitosa.
    // 'errorcode' contiene el resultado de initgraph. Si es grOk, la inicialización fue correcta.
    errorcode = graphresult();

    // Si hubo un error al iniciar el modo gráfico, muestra un mensaje de error y espera a que se presione una tecla antes de salir.
    if (errorcode != grOk)
    {
        printf("ERROR GRAFICO: %s\n", grapherrormsg(errorcode));  // Muestra el mensaje de error correspondiente.
        printf("Presionar alguna tecla para salir: ");           // Pide al usuario que presione una tecla para continuar.
        getch();                                                  // Espera a que se presione una tecla.
        exit(1);                                                  // Sale del programa con un código de error.
    }

    // Dibuja una línea diagonal desde la esquina superior izquierda (0,0) hasta la esquina inferior derecha de la pantalla.
    line(0, 0, getmaxx(), getmaxy());

    // Espera a que el usuario presione una tecla antes de continuar.
    getch();

    // Cierra el modo gráfico y regresa al modo texto.
    closegraph();

    // Sale del programa con un código de éxito (0).
    return(0);
}
