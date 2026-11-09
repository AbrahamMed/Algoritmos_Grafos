def floyd_warshall(grafo, nodos):
    distancias = {u: {v: float('inf') for v in nodos} for u in nodos}
    
    for u in nodos:
        distancias[u][u] = 0
        for vecino, peso in grafo.get(u, {}).items():
            distancias[u][vecino] = peso
            
    for k in nodos:
        for i in nodos:
            for j in nodos:
                if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
                    
    return distancias

nodos_ejemplo = ['A', 'B', 'C', 'D', 'E']
grafo_ejemplo = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'B': 1, 'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

resultado = floyd_warshall(grafo_ejemplo, nodos_ejemplo)

print("=" * 45)
print("   MATRIZ DE DISTANCIAS MÍNIMAS (FLOYD)   ")
print("=" * 45)

print("    ", end="")
for nodo in nodos_ejemplo:
    print(f"[{nodo}]  ", end="")
print("\n" + "-" * 45)

for u in nodos_ejemplo:
    print(f"[{u}]", end="")
    for v in nodos_ejemplo:
        val = resultado[u][v]
        texto = str(val) if val != float('inf') else "∞"
        print(f"{texto:>5} ", end="")
    print()

print("=" * 45)
