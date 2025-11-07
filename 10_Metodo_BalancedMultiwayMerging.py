def BalancedMultiwayMerging(arr, k=3):
    # Divide el arreglo en 'k' runs del mismo tamaño aproximado
    n = len(arr)
    size = n // k + (n % k > 0)
    runs = [arr[i:i+size] for i in range(0, n, size)]

    # Ordenar cada run individual antes de mezclar
    runs = [sorted(run) for run in runs]

    # Mezclar de muchas vías hasta quedar un run final
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), k):
            group = runs[i:i+k]
            new_runs.append(multi_merge(group))
        runs = new_runs

    return runs[0]

def multi_merge(runs):
    result = []
    indices = [0] * len(runs)
    
    # Mientras haya elementos en alguno de los runs
    while True:
        min_val = None
        min_idx = -1
        
        # Encontrar el menor valor disponible
        for i, run in enumerate(runs):
            if indices[i] < len(run):
                val = run[indices[i]]
                if min_val is None or val < min_val:
                    min_val = val
                    min_idx = i
        
        if min_idx == -1:
            break
        
        result.append(min_val)
        indices[min_idx] += 1

    return result
