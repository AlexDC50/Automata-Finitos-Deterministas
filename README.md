# Automata-Finitos-Deterministas

Código de autómata de Moorel / Mealy que fue realizado en clase de la actividad asignada por el maestro donde el flujo de 1 y 0 reciben cada vez una secuencia de 11 por lo cual se reemplaza por 00.

1. Estado inicial: Representa el reposo del sistema o la recepción de un bit 0 a lo cual su salida esta
   asociada al 0.

2. Estado de primer bit: Al recibir el primer 1 se diferencia de un repetidor simple donde este diseño
   de Moore asigna preventivamente una salida 0 este estado anticipa el reemplazo.

3. Estado de reemplazo: El automata detecta el segundo 1 de forma consecutiva al estar en estado del sistema que emite un 0 completando asi la sustitución de la secuencia 11 por 00 en el flujo de salida.
