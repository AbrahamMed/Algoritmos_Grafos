class UnionFind:
    def __init__(self, nodos):
        self.padre = {nodo: nodo for nodo in nodos}
        self.rango = {nodo: 0 for nodo in nodos}

    def buscar(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.buscar(self.padre[nodo])
        return self.padre[nodo]

    def union(self, u, v):
        raiz_u = self.buscar(u)
        raiz_v = self.buscar(v)
        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            elif self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1
            return True
        return False

def kruskal(nodos, aristas):
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])
    uf = UnionFind(nodos)
    mst = []
    costo_total = 0

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            costo_total += peso
            if len(mst) == len(nodos) - 1:
                break
                
    return mst, costo_total

nodos_ejemplo = ['A', 'B', 'C', 'D', 'E']
aristas_ejemplo = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'E', 2)
]

mst, costo = kruskal(nodos_ejemplo, aristas_ejemplo)

print("=" * 40)
print("     ÁRBOL DE EXPANSIÓN MÍNIMA (KRUSKAL)     ")
print("=" * 40)
print(f" {'Conexión':<15} | {'Peso':<10}")
print("-" * 40)

for u, v, peso in mst:
    print(f"  [{u}] <---> [{v}]  |  {peso:<10}")

print("-" * 40)
print(f" COSTO TOTAL DEL MST: {costo}")
print("=" * 40)
