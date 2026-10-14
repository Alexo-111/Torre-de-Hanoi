"""Torre de Hanoi - Estructura de Datos.

Cada torre es una PILA (stack) implementada con una lista de Python:
append() = push, pop() = pop.
"""
import sys
import time


class TorreHanoi:
    def __init__(self, n_discos):
        self.n = n_discos
        # Torre A tiene todos los discos (el mayor abajo), B y C vacías
        self.torres = {"A": list(range(n_discos, 0, -1)), "B": [], "C": []}
        self.movimientos = 0

    def mover_disco(self, origen, destino):
        """Pasa el disco de arriba de una torre a otra (pop + push)."""
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos += 1

    def resolver(self, n=None, origen="A", auxiliar="B", destino="C"):
        """Solución recursiva clásica."""
        if n is None:
            n = self.n
        if n == 0:
            return
        self.resolver(n - 1, origen, destino, auxiliar)
        self.mover_disco(origen, destino)
        self.resolver(n - 1, auxiliar, origen, destino)

    def mostrar_torres(self):
        """Imprime el estado actual de las tres torres."""
        for nombre, pila in self.torres.items():
            print(f"Torre {nombre}: {pila}")

    def movimientos_minimos(self):
        """Fórmula teórica: 2^n - 1."""
        return 2 ** self.n - 1


def medir_tiempo(n_discos):
    """Resuelve el juego y regresa (movimientos, segundos)."""
    juego = TorreHanoi(n_discos)
    inicio = time.perf_counter()
    juego.resolver()
    fin = time.perf_counter()
    return juego.movimientos, fin - inicio


def formatear(segundos):
    unidades = [("años", 31_557_600), ("días", 86_400), ("horas", 3_600),
                ("minutos", 60)]
    for nombre, valor in unidades:
        if segundos >= valor:
            return f"{segundos / valor:,.2f} {nombre}"
    return f"{segundos:.6f} segundos"


if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    casos = [int(x) for x in sys.argv[1:]] or [5, 10, 30]
    movs_por_seg = None

    print(f"{'Discos':>7} | {'Movimientos':>26} | Tiempo")
    print("-" * 70)
    for n in casos:
        movs, t = medir_tiempo(n)
        movs_por_seg = movs / t if t > 0 else movs_por_seg
        print(f"{n:>7} | {movs:>26,} | {formatear(t)}")

    # 64 discos: no se ejecuta, se estima con la velocidad medida
    if movs_por_seg:
        movs64 = 2 ** 64 - 1
        print(f"{64:>7} | {movs64:>26,} | ~{formatear(movs64 / movs_por_seg)} (estimado)")
