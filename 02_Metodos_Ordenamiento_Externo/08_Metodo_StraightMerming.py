def merge_dos_runs(run1, run2):
    """Función auxiliar que fusiona dos 'runs' (listas) ordenados."""
    resultado = []
    i = j = 0
    while i < len(run1) and j < len(run2):
        if run1[i] < run2[j]:
            resultado.append(run1[i])
            i += 1
        else:
            resultado.append(run2[j])
            j += 1
    # Agregar los elementos restantes
    resultado.extend(run1[i:])
    resultado.extend(run2[j:])
    return resultado

def straight_merging_simulado(runs_iniciales):
    """
    Simula una fusión directa (Straight Merging) de 2 vías.
    'runs_iniciales' es una lista de listas (simulando los archivos en disco).
    """
    print(f"Runs Iniciales: {runs_iniciales}")
    
    runs = runs_iniciales
    
    # Repetir mientras haya más de 1 run
    while len(runs) > 1:
        nuevos_runs = []
        # Tomar los runs de 2 en 2
        for i in range(0, len(runs), 2):
            run1 = runs[i]
            # Verificar si hay un segundo run para fusionar
            if (i + 1) < len(runs):
                run2 = runs[i+1]
                run_fusionado = merge_dos_runs(run1, run2)
                nuevos_runs.append(run_fusionado)
            else:
                # Si hay un run impar, simplemente pasa a la siguiente ronda
                nuevos_runs.append(run1)
        
        runs = nuevos_runs # Los runs fusionados son la entrada de la siguiente pasada
        print(f"Siguiente pasada de fusión: {runs}")
        
    # Al final, 'runs' tendrá una sola lista con todo ordenado
    return runs[0]

# --- Ejemplo de uso ---
# Estos serían los "runs" creados en la Fase 1 (ordenados en RAM y escritos a disco)
print("Ejemplo de Straight Merging Simulado:")
runs_fase_1 = [[5, 10], [1, 7], [3, 8], [2, 9], [4, 6]]
ordenada = straight_merging_simulado(runs_fase_1)
print(f"Straight Merging (Resultado Final): {ordenada}\n")