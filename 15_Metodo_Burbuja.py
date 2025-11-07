def Burbuja(arr):
    n = len(arr)
    
    # Hacemos n pasadas
    for i in range(n):
        for j in range(0, n - 1):
            # Si está desordenado → intercambio
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
