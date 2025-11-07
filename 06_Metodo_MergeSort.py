def MergeSort(arr):
    # Si hay 1 o 0 elementos, está ordenado
    if len(arr) <= 1:
        return arr
    
    # Dividimos el arreglo en 2 mitades
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    
    # Combinamos ambas mitades ordenadas
    return merge(left, right)

# Función de mezcla (merge)
def merge(left, right):
    result = []
    i = j = 0
    
    # Comparamos elementos y agregamos el menor primero
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Agregamos elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result
