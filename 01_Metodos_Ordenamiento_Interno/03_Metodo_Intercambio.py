def bubble_sort(arr):
    """
    Ordena una lista usando el método de Burbuja (Intercambio).
    Compara repetidamente pares de elementos adyacentes y
    los intercambia si están en el orden incorrecto.
    """
    n = len(arr)
    
    # Recorrer todos los elementos
    for i in range(n):
        # Un indicador para optimizar: si en una pasada
        # no hay intercambios, la lista ya está ordenada.
        intercambio_hecho = False
        
        # Recorrer la lista desde el inicio hasta n-i-1
        # (los últimos i elementos ya están en su lugar)
        for j in range(0, n - i - 1):
            
            # Comparar elementos adyacentes
            if arr[j] > arr[j + 1]:
                # Intercambiar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio_hecho = True
                
        # Si no se hizo ningún intercambio, parar.
        if not intercambio_hecho:
            break
    return arr

# --- Ejemplo de uso ---
print("Ejemplo de Bubble Sort:")
lista_ejemplo = [5, 1, 4, 2, 8]
print(f"Bubble Sort (Original): {lista_ejemplo}")
ordenada = bubble_sort(lista_ejemplo.copy())
print(f"Bubble Sort (Ordenada): {ordenada}\n")