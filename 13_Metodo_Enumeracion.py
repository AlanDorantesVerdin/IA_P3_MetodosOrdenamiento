# Compara cada elemento con todos para saber cuántos son menores
def Enumeracion(arr):
    n = len(arr)
    result = [0] * n
    
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] < arr[i]:
                count += 1
        
        # Ubica el elemento en la posición que corresponde
        result[count] = arr[i]
    
    return result
