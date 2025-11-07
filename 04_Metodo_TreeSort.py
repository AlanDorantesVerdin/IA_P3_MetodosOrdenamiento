# Nodo básico para un Árbol Binario de Búsqueda (BST)
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

# Inserta un valor en el árbol siguiendo reglas del BST
def insertar(root, valor):
    if root is None:
        return Node(valor)
    
    if valor < root.valor:
        root.left = insertar(root.left, valor)
    else:
        root.right = insertar(root.right, valor)
    
    return root

# Recorremos el árbol en orden (in-order traversal) para obtener una lista ordenada
def recorrer_inorder(root, arr):
    if root:
        recorrer_inorder(root.left, arr)
        arr.append(root.valor)
        recorrer_inorder(root.right, arr)

# Función principal de Tree Sort
def TreeSort(arr):
    root = None
    
    # Insertar todos los valores en el árbol
    for v in arr:
        root = insertar(root, v)
    
    # Obtener valores ya ordenados mediante recorrido inorder
    sorted_arr = []
    recorrer_inorder(root, sorted_arr)
    return sorted_arr
