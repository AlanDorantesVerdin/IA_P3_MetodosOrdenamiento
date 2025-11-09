def merge_sort(arr):
    """
    Ordena una lista usando el método MergeSort (Divide y Vencerás).
    """
    if len(arr) > 1:
        # 1. Dividir
        medio = len(arr) // 2
        mitad_izquierda = arr[:medio]
        mitad_derecha = arr[medio:]

        # 2. Vencerás (Recursión)
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        # 3. Combinar (Merge)
        i = j = k = 0
        
        # Combinar las dos mitades ordenadas de vuelta en 'arr'
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                arr[k] = mitad_izquierda[i]
                i += 1
            else:
                arr[k] = mitad_derecha[j]
                j += 1
            k += 1

        # Copiar los elementos restantes (si los hay)
        while i < len(mitad_izquierda):
            arr[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            arr[k] = mitad_derecha[j]
            j += 1
            k += 1
    
    # Importante: MergeSort ordena la lista "in-place" (en el lugar)
    # Por eso no devuelve nada, modifica 'arr' directamente.

# --- Ejemplo de uso ---
print("Ejemplo de MergeSort:")
lista_ejemplo = [12, 11, 13, 5, 6, 7]
print(f"MergeSort (Original): {lista_ejemplo}")
# Hacemos una copia porque la función modifica la lista original
copia_lista = lista_ejemplo.copy()
merge_sort(copia_lista)
print(f"MergeSort (Ordenada): {copia_lista}\n")