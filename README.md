# Práctica 2: Métodos de Ordenamiento (IA)

Este repositorio contiene la implementación de diversos algoritmos de ordenamiento, tanto internos como externos, como parte de la Práctica 2 de la materia de Inteligencia Artificial.

El proyecto incluye:
* Implementaciones en Python de algoritmos de ordenamiento interno.
* Simulaciones conceptuales de algoritmos de ordenamiento externo.

---

## Algoritmos Implementados

Los scripts están divididos por tipo de ordenamiento.

### 1. Ordenamiento Interno
(Se ejecutan completamente en la memoria RAM)

* **Inserción (Insertion Sort):** Eficiente para listas pequeñas o casi ordenadas.
* **Selección (Selection Sort):** Simple, pero ineficiente (O(n²)).
* **Intercambio (Bubble Sort):** Clásico algoritmo didáctico.
* **Ordenamiento de Árbol (Tree Sort):** Usa un Árbol Binario de Búsqueda (BST).
* **QuickSort:** Algoritmo "Divide y Vencerás" muy rápido en promedio.
* **MergeSort:** "Divide y Vencerás" con rendimiento estable (O(n log n)).
* **RadixSort:** Ordenamiento no comparativo basado en dígitos.

### 2. Ordenamiento Externo (Simulaciones)
(Técnicas para datos que no caben en RAM, simuladas usando listas)

* **Creación de "Runs" Naturales:** Estrategia de Fase 1 para crear tramos ordenados iniciales.
* **Straight Merging (Fusión Directa):** Fusión simple de 2 vías.
* **Balanced Multiway Merging (Fusión K-vías):** Fusión de K "runs" simultáneamente (simulada con `heapq`).
* **Polyphase Sort (Fusión Polifásica):** Técnica avanzada de fusión que minimiza el uso de "cintas" (archivos).
* **Distribution of Initial Runs:** Lógica para la distribución estratégica de "runs" (Balanceada y tipo Fibonacci para Polyphase).

---

## Autor

* **Alan Dorantes Verdin** - [AlanDorantesVerdin](https://github.com/AlanDorantesVerdin)