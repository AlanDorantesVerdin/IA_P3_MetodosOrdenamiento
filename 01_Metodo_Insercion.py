def InsertionSort(arr):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        temp = arr[i]  # Guardamos el elemento actual
        j = i - 1
        
        # Movemos elementos mayores que temp una posición adelante
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertamos el elemento en la posición correcta
        arr[j + 1] = temp

    return arr
