# --- Primero, definimos la estructura del Nodo y el Árbol ---
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, valor):
    """Función recursiva para insertar un valor en el BST."""
    if raiz is None:
        return Nodo(valor)
    
    if valor < raiz.valor:
        raiz.izquierda = insertar(raiz.izquierda, valor)
    else:
        # Nota: Permite duplicados, insertándolos a la derecha
        raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

def recorrido_in_order(raiz, lista_ordenada):
    """
    Recorre el árbol In-Order (Izq - Raíz - Der)
    y va guardando los valores en una lista.
    """
    if raiz:
        recorrido_in_order(raiz.izquierda, lista_ordenada)
        lista_ordenada.append(raiz.valor)
        recorrido_in_order(raiz.derecha, lista_ordenada)

# --- Ahora, la función de Tree Sort ---
def tree_sort(arr):
    """
    Ordena una lista usando un Árbol Binario de Búsqueda.
    1. Construye el árbol insertando todos los elementos.
    2. Realiza un recorrido In-Order para obtener la lista ordenada.
    """
    if not arr:
        return []
    
    # 1. Construir el árbol
    raiz = Nodo(arr[0])
    for i in range(1, len(arr)):
        insertar(raiz, arr[i])
        
    # 2. Realizar recorrido In-Order
    lista_ordenada = []
    recorrido_in_order(raiz, lista_ordenada)
    return lista_ordenada

# --- Ejemplo de uso ---
print("Ejemplo de Tree Sort:")
lista_ejemplo = [8, 3, 10, 1, 6, 14, 4, 7, 13]
print(f"Tree Sort (Original): {lista_ejemplo}")
ordenada = tree_sort(lista_ejemplo.copy())
print(f"Tree Sort (Ordenada): {ordenada}\n")