def DistributionInitialRuns(arr):
    # Generación de runs naturales
    runs = []
    temp = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            temp.append(arr[i])
        else:
            runs.append(temp)
            temp = [arr[i]]
    runs.append(temp)

    # Distribución simulada en 3 archivos (listas)
    files = [[], [], []]
    f = 0
    for run in runs:
        files[f].append(run)
        f = (f + 1) % 3

    # Mezclar archivos hasta ser uno solo
    result = []
    for f in files:
        for run in f:
            result = merge(result, run)

    return result
