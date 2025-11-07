def ShellSort(arr):
    n = len(arr)
    gap = n // 2  # Tamaño inicial del salto
    
    # Reducimos el gap progresivamente
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Inserción pero con saltos de "gap"
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2  # Reducimos el salgo a la mitad
    
    return arr
