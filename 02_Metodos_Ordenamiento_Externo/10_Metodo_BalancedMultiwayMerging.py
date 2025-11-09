import heapq

def balanced_multiway_merging_simulado(runs_iniciales):
    """
    Simula una fusión K-vías balanceada usando heapq.merge.
    'heapq.merge' toma K iterables ordenados y los fusiona
    en un solo iterable ordenado de manera muy eficiente (usando un min-heap).
    
    En un escenario real, 'runs_iniciales' serían K archivos abiertos
    y estaríamos leyendo un elemento a la vez de cada uno.
    """
    print(f"Runs Iniciales (K={len(runs_iniciales)}): {runs_iniciales}")
    
    # heapq.merge es el corazón de una fusión K-vías
    # El *args (runs_iniciales) desempaqueta la lista de listas
    # como argumentos separados para la función merge.
    iterable_ordenado = heapq.merge(*runs_iniciales)
    
    # Convertir el iterable resultante de vuelta a una lista
    return list(iterable_ordenado)

# --- Ejemplo de uso ---
# Simulando una fusión de 5 vías (K=5)
print("Ejemplo de Balanced Multiway Merging Simulado:")
runs_fase_1 = [
    [10, 20, 30],      # Run 1 (Archivo 1)
    [5, 15, 25],       # Run 2 (Archivo 2)
    [1, 11, 22],       # Run 3 (Archivo 3)
    [8, 18, 28],       # Run 4 (Archivo 4)
    [2, 12, 24]        # Run 5 (Archivo 5)
]
ordenada = balanced_multiway_merging_simulado(runs_fase_1)
print(f"Multiway Merging (Resultado Final): {ordenada}\n")