def distribute_for_balanced_merging(all_runs, K):
    """
    Implementa la ESTRATEGIA de "Distribución de initial runs"
    para un algoritmo de Fusión Balanceada de K-vías.
    
    Toma una lista de 'runs' y los distribuye de forma
    equitativa (round-robin) entre 'K' cintas simuladas.
    
    Args:
        all_runs (list): Una lista de listas (ej. [[1,5], [2,7], [3,6]...])
        K (int): El número de "cintas" o "archivos" de entrada disponibles.
        
    Returns:
        list: Una lista que contiene K listas (las cintas),
              cada una con su subconjunto de runs.
    """
    
    print("Ejemplo de Distribución para Fusión Balanceada:\n")
    print(f"--- Iniciando Distribución Balanceada (K={K}) ---")
    print(f"Total de runs a distribuir: {len(all_runs)}")
    
    # 1. Crear las K cintas de entrada (inicialmente vacías)
    #    (En nuestra simulación, es una lista de K listas)
    tapes = [[] for _ in range(K)]
    
    # 2. Distribuir los runs uno por uno (Round-Robin)
    for i, run in enumerate(all_runs):
        
        # El operador módulo (%) es perfecto para "round-robin"
        # i = 0 -> 0 % K = 0 (Cinta 0)
        # i = 1 -> 1 % K = 1 (Cinta 1)
        # ...
        # i = K -> K % K = 0 (Cinta 0 de nuevo)
        tape_index = i % K
        
        print(f"Run {i} {run} -> Cinta {tape_index}")
        
        # Añadir el run a la cinta correspondiente
        tapes[tape_index].append(run)
        
    print("\n--- Distribución Finalizada ---")
    for i, tape_content in enumerate(tapes):
        print(f"  Cinta {i}: {len(tape_content)} runs -> {tape_content}")
        
    return tapes

# --- Ejemplo de uso ---

# Usemos los "runs naturales" de un ejemplo anterior
runs_naturales = [[1, 5, 8], [2, 4, 9], [3, 6, 7, 10], [0], [11, 20], [15]]

# Vamos a distribuirlos entre K=3 cintas de entrada
K = 3
distribucion_balanceada = distribute_for_balanced_merging(runs_naturales, K)

print("\nContenido final de las cintas simuladas:")
print(distribucion_balanceada)
print("")