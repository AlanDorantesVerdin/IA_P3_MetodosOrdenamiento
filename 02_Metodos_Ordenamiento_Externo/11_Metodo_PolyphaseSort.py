def distribute_for_polyphase(runs):
    """
    Distribuye los 'runs' iniciales para un Polyphase Sort
    de 3 cintas (2 de entrada, 1 de salida) usando números de Fibonacci.
    
    Devuelve los 'runs' para la cinta 1 y la cinta 2.
    """
    n = len(runs)
    
    # 1. Encontrar el número de Fibonacci (Fn) >= n
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    Fn = fib[-1]
    Fn_minus_1 = fib[-2]
    Fn_minus_2 = fib[-3] # (Fn_minus_2 = Fn - Fn_minus_1)
    
    print(f"Distribución: Se necesitan {Fn} runs (Fibonacci). Se tienen {n}.")
    
    # 2. Añadir "dummy runs" (runs vacíos) si n no es un Fn
    num_dummies = Fn - n
    if num_dummies > 0:
        print(f"Añadiendo {num_dummies} 'dummy runs' (vacíos).")
        # En una simulación, añadimos listas vacías
        runs.extend([[] for _ in range(num_dummies)])
        
    # 3. Distribuir los runs
    # La distribución ideal es Fn-1 y Fn-2
    # (Ej: para 13 runs, se distribuyen 8 y 5)
    
    runs_cinta_1 = runs[:Fn_minus_1]
    runs_cinta_2 = runs[Fn_minus_1:]
    
    print(f"Distribuidos {len(runs_cinta_1)} runs en Cinta 1 y {len(runs_cinta_2)} runs en Cinta 2.")
    
    return runs_cinta_1, runs_cinta_2

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
    resultado.extend(run1[i:])
    resultado.extend(run2[j:])
    return resultado

def polyphase_sort_simulado(runs_iniciales):
    """
    Simula una Fusión Polifásica (Polyphase Sort) usando 3 "cintas".
    """
    
    # 1. Distribuir los runs
    runs_cinta_1, runs_cinta_2 = distribute_for_polyphase(runs_iniciales)
    
    # Las 'cintas' serán un diccionario.
    # cintas[1] y cintas[2] son entrada, cintas[3] es salida (inicialmente vacía)
    cintas = {
        1: runs_cinta_1,
        2: runs_cinta_2,
        3: []
    }
    
    # Índices para saber quién es entrada y quién es salida
    idx_in1 = 1
    idx_in2 = 2
    idx_out = 3
    
    pasada = 1
    
    # 2. Bucle de Fusión (El "baile de las cintas")
    # Continuar mientras haya más de una cinta con runs
    while len(cintas[idx_in1]) > 0 and len(cintas[idx_in2]) > 0:
        
        print(f"\n--- Pasada de Fusión {pasada} ---")
        print(f"Fusionando {len(cintas[idx_in1])} runs de C{idx_in1} y {len(cintas[idx_in2])} runs de C{idx_in2} -> C{idx_out}")
        
        # Determinar cuántos runs fusionar (el mínimo de las dos cintas de entrada)
        num_a_fusionar = min(len(cintas[idx_in1]), len(cintas[idx_in2]))
        
        # Realizar la fusión
        for _ in range(num_a_fusionar):
            run1 = cintas[idx_in1].pop(0) # Saca el primer run de la cinta 1
            run2 = cintas[idx_in2].pop(0) # Saca el primer run de la cinta 2
            
            run_fusionado = merge_dos_runs(run1, run2)
            
            cintas[idx_out].append(run_fusionado) # Añade el run fusionado a la cinta de salida
            
        print(f"Estado: C1={len(cintas[1])} | C2={len(cintas[2])} | C3={len(cintas[3])}")
        
        # 3. Rotar las cintas
        # La cinta que se vació se convierte en la NUEVA cinta de salida.
        # La antigua cinta de salida se convierte en una de entrada.
        
        if len(cintas[idx_in1]) == 0:
            # La cinta in1 se vació. Ahora es la salida.
            # La antigua salida (out) es ahora la nueva in1.
            idx_in1, idx_out = idx_out, idx_in1
        elif len(cintas[idx_in2]) == 0:
            # La cinta in2 se vació. Ahora es la salida.
            # La antigua salida (out) es ahora la nueva in2.
            idx_in2, idx_out = idx_out, idx_in2
            
        pasada += 1
        
    # Al final, una sola cinta tendrá 1 run con todos los datos.
    # Encontrar la cinta que no está vacía.
    cinta_final = idx_in1 if len(cintas[idx_in1]) > 0 else idx_in2
    if not cintas[cinta_final]: # Por si acaso quedó en la idx_out
        cinta_final = idx_out
        
    print(f"\nFusión completada. El resultado está en la Cinta {cinta_final}.")
    
    # El resultado es el primer (y único) run en la cinta final
    if len(cintas[cinta_final]) > 0:
        return cintas[cinta_final][0]
    else:
        return [] # Caso de entrada vacía

# --- Ejemplo de uso de Polyphase Sort ---
print("Ejemplo de Polyphase Sort Simulado:\n")

# 1. Datos iniciales (podrían ser cualquier conjunto de runs)
#    Usaremos los 'runs naturales' del ejemplo 1
runs_iniciales = [[1, 5, 8], [2, 4, 9], [3, 6, 7, 10], [0]]
print(f"Runs iniciales para fusionar: {runs_iniciales}")

# 2. Ejecutar la simulación de Fusión Polifásica
resultado_final = polyphase_sort_simulado(runs_iniciales)

print(f"\nResultado Final Ordenado: {resultado_final}\n")