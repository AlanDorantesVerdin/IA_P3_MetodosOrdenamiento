def PolyphaseSort(arr):
    # Se generan runs iniciales a partir de datos ordenados naturalmente
    runs = split_into_polyphase_runs(arr)

    # Mezclar respetando tamaños iniciales (simulación)
    while len(runs) > 1:
        # Tomar los dos primeros runs, mezclarlos y reinsertar ordenadamente
        a = runs.pop(0)
        b = runs.pop(0)
        runs.append(merge(a, b))
        runs.sort(key=len)  # Sigue el comportamiento de Polyphase

    return runs[0]

def split_into_polyphase_runs(arr):
    runs = []
    temp = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            temp.append(arr[i])
        else:
            runs.append(temp)
            temp = [arr[i]]
    runs.append(temp)

    runs.sort(key=len)  # Polyphase requiere runs desbalanceados
    return runs
