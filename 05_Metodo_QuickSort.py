def QuickSort(arr):
    # Caso base: si hay 1 o 0 elementos ya está ordenado
    if len(arr) <= 1:
        return arr
    
    # Elegimos un pivote (centro para simplicidad)
    pivot = arr[len(arr) // 2]

    # Dividimos en 3 partes:
    # menores, iguales al pivote y mayores
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Ordenamos recursivamente y combinamos
    return QuickSort(left) + mid + QuickSort(right)
