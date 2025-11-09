def counting_sort_para_radix(arr, exponente):
    """
    Función auxiliar de Counting Sort para ordenar 'arr'
    basándose en el dígito especificado por 'exponente' (1, 10, 100...).
    """
    n = len(arr)
    # Lista de salida
    salida = [0] * n
    # Lista de conteo (para dígitos 0-9)
    conteo = [0] * 10
    
    # 1. Contar ocurrencias de cada dígito
    for i in range(n):
        # Obtener el dígito (ej. 170, exp 1 -> 0; exp 10 -> 7; exp 100 -> 1)
        indice = (arr[i] // exponente) % 10
        conteo[indice] += 1
        
    # 2. Modificar el conteo para que contenga las posiciones finales
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
        
    # 3. Construir la lista de salida
    # (Se itera en reversa para mantener la estabilidad)
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exponente) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1
        
    # 4. Copiar la salida a 'arr'
    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    """
    Ordena una lista de enteros positivos usando RadixSort.
    """
    # Encontrar el número máximo para saber cuántos dígitos tiene
    maximo = max(arr)
    
    # 'exponente' será 1, 10, 100...
    # Se aplica counting sort para cada dígito
    exponente = 1
    while maximo // exponente > 0:
        counting_sort_para_radix(arr, exponente)
        exponente *= 10
        
    # La lista 'arr' se modifica in-place

# --- Ejemplo de uso ---
print("Ejemplo de Radix Sort:")
lista_ejemplo = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"RadixSort (Original): {lista_ejemplo}")
copia_lista = lista_ejemplo.copy()
radix_sort(copia_lista)
print(f"RadixSort (Ordenada): {copia_lista}\n")