def Intercambio(arr):
    n = len(arr)
    cambiado = True
    
    # Repetimos hasta que ya no se hagan más intercambios
    while cambiado:
        cambiado = False
        
        # Comparamos pares consecutivos
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                # Si están en orden incorrecto → intercambiamos
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                cambiado = True
    
    return arr
