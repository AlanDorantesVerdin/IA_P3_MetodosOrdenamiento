def SelectionSort(arr):
    n = len(arr)
    
    # Seleccionamos la posición donde irá el siguiente menor valor
    for i in range(n):
        min_i = i  # Suponemos que el menor está en i
        
        # Buscamos si hay otro valor menor en el resto del arreglo
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        
        # Intercambiamos el menor encontrado con la posición actual
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr
