def warshall(grafo, nodos):
    matriz = {u: {v: 0 for v in nodos} for u in nodos}
    
    for u in nodos:
        matriz[u][u] = 1
        for vecino in grafo.get(u, {}):
            matriz[u][vecino] = 1
            
    for k in nodos:
        for i in nodos:
            for j in nodos:
                matriz[i][j] = matriz[i][j] or (matriz[i][k] and matriz[k][j])
                
    return matriz

nodos_ejemplo = ['A', 'B', 'C', 'D', 'E']
grafo_ejemplo = {
    'A': {'B': 1, 'C': 1},
    'B': {'C': 1, 'D': 1},
    'C': {'B': 1, 'D': 1, 'E': 1},
    'D': {'E': 1},
    'E': {}
}

resultado = warshall(grafo_ejemplo, nodos_ejemplo)

print("=" * 35)
print("  MATRIZ DE CONECTIVIDAD (WARSHALL)  ")
print("=" * 35)

print("    ", end="")
for nodo in nodos_ejemplo:
    print(f"[{nodo}] ", end="")
print("\n" + "-" * 35)

for u in nodos_ejemplo:
    print(f"[{u}]", end="")
    for v in nodos_ejemplo:
        print(f"{resultado[u][v]:>4} ", end="")
    print()

print("=" * 35)
