def selection_sort(arr):
    """
    Ordena una lista usando el método de Selección.
    Busca repetidamente el elemento mínimo en la parte no ordenada
    y lo intercambia con el primer elemento de esa parte.
    """
    n = len(arr)
    
    # Recorrer toda la lista
    for i in range(n):
        # Encontrar el índice del elemento mínimo en la
        # sub-lista no ordenada (desde i hasta el final)
        idx_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx_minimo]:
                idx_minimo = j
                
        # Intercambiar el elemento mínimo encontrado con el
        # primer elemento de la sub-lista no ordenada (posición i)
        arr[i], arr[idx_minimo] = arr[idx_minimo], arr[i]
        
    return arr

# --- Ejemplo de uso ---
print("Ejemplo de Selection Sort:")
lista_ejemplo = [64, 25, 12, 22, 11]
print(f"Selection Sort (Original): {lista_ejemplo}")
ordenada = selection_sort(lista_ejemplo.copy())
print(f"Selection Sort (Ordenada): {ordenada}\n")