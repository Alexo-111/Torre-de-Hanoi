# Torre de Hanoi en Python

## Métodos que maneja

La clase `TorreHanoi` tiene **5 métodos** (4 de instancia, incluyendo el constructor,
más `movimientos_minimos`), y el programa tiene **2 funciones auxiliares**:

| # | Método | Qué hace |
|---|--------|----------|
| 1 | `__init__(n_discos)` | Crea las 3 torres (pilas). La torre A inicia con todos los discos. |
| 2 | `mover_disco(origen, destino)` | Quita el disco de arriba de una pila (`pop`) y lo pone en otra (`append`). Cuenta el movimiento. |
| 3 | `resolver(n, origen, auxiliar, destino)` | Solución **recursiva**: mueve n-1 discos al auxiliar, mueve el mayor y vuelve a mover los n-1 encima. |
| 4 | `mostrar_torres()` | Imprime el contenido actual de las tres torres. |
| 5 | `movimientos_minimos()` | Regresa la fórmula teórica 2ⁿ − 1. |

Funciones auxiliares fuera de la clase: `medir_tiempo(n_discos)` (usa
`time.perf_counter()`) y `formatear(segundos)` (convierte segundos a
minutos, días, años, etc.).

## Resultados de la ejecución

Medido con Python 3.12.3, x86_64, 1 núcleo (sin imprimir movimientos).

| Discos | Movimientos (2ⁿ − 1) | Tiempo |
|-------:|---------------------:|--------|
| 5  | 31 | 0.000054 s |
| 10 | 1,023 | 0.000354 s |
| 30 | 1,073,741,823 | 3.78 min |
| 64 | 18,446,744,073,709,551,615 | ~123,508 años (**estimado**, no ejecutado) |

> Los 64 discos no se ejecutaron: se estimó dividiendo los movimientos
> necesarios entre la velocidad medida (~4.7 millones de movimientos por segundo).

## Conclusiones

1. **Crecimiento exponencial**: El número de movimientos es 2ⁿ − 1, Por lo que cada disco añadido implica un crecimiento exponencial en la cantidad de movimientos para completar el juego. La complejidad es **O(2ⁿ)**.
2. **Pasar de 5 a 30 discos**: (6 veces más discos) con este cambio se hace notoria una diferencia de tiempo considerable con respecto a pruebas con 5 y 10 discos, implica un aumento de millones de veces en la cantidad de movimientos a realizar para trasladar la torre correctamente.
3. **64 discos es inviable**: a pesar de la cantidad de movimientos por segundo que puede realizar el procesador (Tratandose de millones de movimientos por segundo) se vuelve inviable su resolución debido a la ridícula cantidad de movimientos necesarios para realizar el traslado completo de la torre. Por eso la leyenda de los monjes dice que el mundo acaba cuando terminen de mover los 64 discos (Osease nunca).
4. **La recursión no afecta al costo**: (pocas líneas de código), el costo no
   está en la recursión sino en el problema mismo: no existe una solución con
   menos de 2ⁿ − 1 movimientos, así que ningún algoritmo ni lenguaje
   más rápido evita el crecimiento exponencial; solo cambia la constante.
5. **Las pilas son la estructura adecuada**: solo se accede al disco de arriba
   (LIFO), igual que en el juego real, y `append`/`pop` son O(1).
