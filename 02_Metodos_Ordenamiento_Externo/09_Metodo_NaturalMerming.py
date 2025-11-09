def create_natural_runs(datos_completos):
    """
    Simula la creación de "runs" (tramos ordenados) naturales
    a partir de una lista de datos no ordenados.
    
    Lee los datos y sigue añadiendo elementos a un 'run'
    mientras sigan estando en orden ascendente.
    """
    if not datos_completos:
        return []

    runs_generados = []
    run_actual = []
    
    for elemento in datos_completos:
        # Si el run actual está vacío o el nuevo elemento
        # es mayor o igual al último, el run continúa.
        if not run_actual or elemento >= run_actual[-1]:
            run_actual.append(elemento)
        else:
            # Si el elemento rompe el orden (es menor),
            # el run actual se termina y se guarda.
            runs_generados.append(run_actual)
            # Se inicia un nuevo run con el elemento actual.
            run_actual = [elemento]
            
    # No olvides guardar el último run que estaba en progreso.
    if run_actual:
        runs_generados.append(run_actual)
        
    return runs_generados

# --- Ejemplo de uso ---
# Datos como estarían "en disco"
print("Ejemplo de Creación de Runs Naturales:")
datos_en_disco = [1, 5, 8, 2, 4, 9, 3, 6, 7, 10, 0]
print(f"Datos originales: {datos_en_disco}")

runs = create_natural_runs(datos_en_disco)

print("Runs naturales generados:")
for i, run in enumerate(runs):
    print(f"Run {i+1}: {run}")
print("")

# Nota: Después de esto, usarías un método de FASE 2
# (como Straight Merging o Polyphase) sobre estos 'runs'.