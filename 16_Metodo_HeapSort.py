def HeapSort(arr):
    n = len(arr)
    
    # Construimos un Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraemos el mayor y lo ponemos al final del arreglo
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambio
        heapify(arr, i, 0)
    
    return arr

# Mantiene la propiedad de Max-Heap en un subárbol
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2 # Hijo derecho
    
    # Comprobamos si los hijos son mayores
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Si el mayor no es la raíz → se intercambia
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
