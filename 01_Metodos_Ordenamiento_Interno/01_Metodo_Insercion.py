def insertion_sort(arr):
    """
    Ordena una lista usando el método de Inserción.
    Recorre la lista y va "insertando" cada elemento en su
    posición correcta dentro de la sub-lista ya ordenada.
    """
    # Empezamos desde el segundo elemento (índice 1)
    # ya que el primero se considera la lista ordenada inicial.
    for i in range(1, len(arr)):
        
        elemento_actual = arr[i] # El elemento a insertar
        j = i - 1                  # El índice del último elemento de la parte ordenada
        
        # Mover los elementos de la parte ordenada que son mayores
        # que el elemento_actual una posición a la derecha.
        while j >= 0 and elemento_actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Insertar el elemento_actual en su posición correcta
        arr[j + 1] = elemento_actual
        
    return arr

# --- Ejemplo de uso ---
print("Ejemplo de Insertion Sort:")
lista_ejemplo = [12, 11, 13, 5, 6]
print(f"Insertion Sort (Original): {lista_ejemplo}")
ordenada = insertion_sort(lista_ejemplo.copy())
print(f"Insertion Sort (Ordenada): {ordenada}\n")