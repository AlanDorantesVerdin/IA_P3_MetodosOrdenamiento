def RadixSort(arr):
    # Obtenemos el número más grande para saber el número de dígitos
    max_val = max(arr) if arr else 0
    exp = 1  # 1 → unidades, 10 → decenas, 100 → centenas
    
    # Aplicamos counting sort por cada dígito
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10
    
    return arr

# Counting sort específico para un dígito dado (exp)
def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Dígitos del 0 al 9
    
    # Contamos ocurrencias del dígito actual
    for i in arr:
        idx = (i // exp) % 10
        count[idx] += 1
    
    # Transformamos count en posiciones acumuladas
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construimos el arreglo ordenado por ese dígito
    for i in reversed(arr):
        idx = (i // exp) % 10
        output[count[idx] - 1] = i
        count[idx] -= 1
    
    # Copiamos de regreso al arreglo original
    for i in range(n):
        arr[i] = output[i]
