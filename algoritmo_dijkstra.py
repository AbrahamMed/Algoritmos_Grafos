import heapq

def dijkstra(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    cola_prioridad = [(0, origen)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo[nodo_actual].items():
            distancia_total = distancia_actual + peso
            
            if distancia_total < distancias[vecino]:
                distancias[vecino] = distancia_total
                heapq.heappush(cola_prioridad, (distancia_total, vecino))
                
    return distancias

grafo_ejemplo = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'B': 1, 'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

origen = 'A'
resultado = dijkstra(grafo_ejemplo, origen)

print("=" * 35)
print(f"  RUTAS MÁS CORTAS DESDE EL NODO [{origen}]  ")
print("=" * 35)
print(f" {'Destino':<10} | {'Costo Total':<12} | Escala")
print("-" * 35)

for nodo, distancia in resultado.items():
    costo = str(distancia) if distancia != float('inf') else "Inalcanzable"
    print(f"  {nodo:<8} -> | {costo:<12} | {origen} ➔ {nodo}")

print("=" * 35)

