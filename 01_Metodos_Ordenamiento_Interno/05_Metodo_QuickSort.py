def quick_sort(arr):
    """
    Ordena una lista usando el método QuickSort (Divide y Vencerás).
    Implementación recursiva simple.
    """
    if len(arr) <= 1:
        return arr
    else:
        # 1. Elegir un pivote (aquí usamos el primero)
        pivote = arr[0]
        
        # 2. Partición: crear sub-listas de menores y mayores
        menores = [x for x in arr[1:] if x < pivote]
        mayores = [x for x in arr[1:] if x >= pivote]
        
        # 3. Vencerás (Recursión)
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# --- Ejemplo de uso ---
print("Ejemplo de QuickSort:")
lista_ejemplo = [10, 7, 8, 9, 1, 5]
print(f"QuickSort (Original): {lista_ejemplo}")
ordenada = quick_sort(lista_ejemplo.copy())
print(f"QuickSort (Ordenada): {ordenada}\n")