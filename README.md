Algoritmos de Búsqueda



Introducción:

En esta actividad se desarrollan dos métodos para localizar elementos dentro de una lista: búsqueda secuencial y búsqueda binaria.

Ambos algoritmos se implementan en Python y se aplican para encontrar el número 12 en el arreglo "\[1, 3, 4, 6, 12, 15, 35, 44]."



* Búsqueda Secuencial



Este algoritmo revisa los elementos de la lista individualmente, comenzando desde la primera posición y avanzando hasta encontrar el valor solicitado.



Procedimiento paso a paso

Número buscado: 12

1\. Se compara 12 con el primer elemento, 1. No coincide.

2\. Se compara con 3. No coincide.

3\. Se compara con 4. No coincide.

4\. Se compara con 6. No coincide.

5\. Se compara con 12. Se encuentra el elemento y termina la búsqueda.



El número 12 está en el índice 4, correspondiente a la quinta posición del arreglo.



Cantidad de comparaciones: 5.



Complejidad:

\- Mejor caso: O(1), cuando el elemento está al principio.

\- Caso promedio: O(n).

\- Peor caso: O(n), cuando el elemento está al final o no existe.

\- Espacio auxiliar: O(1).



Ventaja: Funciona con listas ordenadas y desordenadas.

Desventaja: Puede necesitar recorrer todos los elementos.



* Búsqueda Binaria



La búsqueda binaria trabaja con listas previamente ordenadas. Su procedimiento consiste en dividir repetidamente el intervalo de búsqueda en dos partes.



Procedimiento paso a paso

Número buscado: 12



1\. Se establece el intervalo de índices 0 a 7. El índice central es 3, cuyo valor es 6. Como 12 es mayor, se continúa por la mitad derecha.

2\. El nuevo intervalo comprende los índices 4 a 7. El índice central es 5, cuyo valor es 15. Como 12 es menor, se continúa por la mitad izquierda.

3\. El intervalo queda reducido al índice 4, cuyo valor es 12. Se encuentra el número buscado.



Resultado: El número 12 se encuentra en el índice 4, correspondiente a la quinta posición.



Cantidad de comparaciones: 3.



Complejidad.

\- Mejor caso: O(1).

\- Caso promedio: O(log n).

\- Peor caso: O(log n).

\- Espacio auxiliar: O(1).



Ventaja: Reduce considerablemente la cantidad de comparaciones.

Desventaja: Requiere que los elementos estén ordenados.



3\. Comparación



Búsqueda Secuencial:

\- Recorre los elementos uno por uno.

\- No necesita que el arreglo esté ordenado.

\- Su complejidad promedio es O(n).

\- Es apropiada para listas pequeñas o desordenadas.

\- En el ejercicio realizó 5 comparaciones.



Búsqueda Binaria:

\- Descarta la mitad del intervalo en cada paso.

\- Necesita un arreglo ordenado.

\- Su complejidad promedio es O(log n).

\- Es recomendable para listas ordenadas con numerosos elementos.

\- En el ejercicio realizó 3 comparaciones.



