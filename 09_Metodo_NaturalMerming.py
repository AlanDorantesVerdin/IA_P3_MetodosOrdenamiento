def NaturalMerging(arr):
    # Paso 1: detectar runs naturales
    runs = []
    temp = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            temp.append(arr[i])
        else:
            runs.append(temp)
            temp = [arr[i]]
    runs.append(temp)

    # Paso 2: mezclar hasta tener solo un run
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                new_runs.append(merge(runs[i], runs[i+1]))
            else:
                new_runs.append(runs[i])
        runs = new_runs
    
    return runs[0]
