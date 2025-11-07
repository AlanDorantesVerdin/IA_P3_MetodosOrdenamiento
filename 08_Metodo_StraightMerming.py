def StraightMerging(arr):
    table = [[x] for x in arr]  # Cada elemento es una lista (run)
    
    # Mientras haya más de un run, mezclar de dos en dos
    while len(table) > 1:
        new_table = []
        
        # Mezcla pareja de runs consecutivos
        for i in range(0, len(table), 2):
            if i + 1 < len(table):
                new_table.append(merge(table[i], table[i+1]))
            else:
                new_table.append(table[i])
        
        table = new_table
    
    return table[0] if table else []
