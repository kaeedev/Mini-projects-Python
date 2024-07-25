<p align="center">INFORMACIÓN</p>

ESP:

Programa con un sistema complejo que incluye múltiples funciones críticas. Para asegurarte de que todo funcione correctamente y para realizar un seguimiento del tiempo de ejecución de estas funciones, implemento un decorador de registro (logger) con tiempo de ejecución.

El decorador realiza las siguientes acciones:

Antes de llamar a la función original, debe imprimir un mensaje indicando que la función está a punto de ejecutarse.

Después de que la función se haya ejecutado, debe imprimir un mensaje que incluya el tiempo que tardó la función en ejecutarse.

Si la función original arroja una excepción, el decorador debe manejarla e imprimir un mensaje adecuado, indicando que se ha producido una excepción.



---

ENG:

Program with a Complex System Including Multiple Critical Functions

To ensure that everything works correctly and to track the execution time of these functions, implement a logging (logger) decorator with execution time tracking.

The decorator performs the following actions:

Before calling the original function, it should print a message indicating that the function is about to execute.

After the function has executed, it should print a message including the time it took for the function to execute.

If the original function raises an exception, the decorator should handle it and print an appropriate message indicating that an exception has occurred.

