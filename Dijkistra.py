import heapq


class Dijkistra:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}

    def adicionar_vertice(self, valor):
        self.vertices.add(valor)
        if valor not in self.arestas:
            self.arestas[valor] = []

    def adicionar_aresta(self, de, para, peso):
        self.adicionar_vertice(de)
        self.adicionar_vertice(para)
        self.arestas[de].append((para, peso))

    def dijkstra(self, origem):
        distancia = {v: float('inf') for v in self.vertices}
        distancia[origem] = 0
        fila = [(0, origem)]
        caminho = {v: [] for v in self.vertices}

        while fila:
            (dist, vertice) = heapq.heappop(fila)
            if dist > distancia[vertice]:
                continue

            for (vizinho, peso) in self.arestas[vertice]:
                if distancia[vertice] + peso < distancia[vizinho]:
                    distancia[vizinho] = distancia[vertice] + peso
                    caminho[vizinho] = caminho[vertice] + [vertice]
                    heapq.heappush(fila, (distancia[vizinho], vizinho))

        return caminho



grafo = Dijkistra()
grafo.adicionar_aresta('A', 'B', 1)
grafo.adicionar_aresta('A', 'C', 4)
grafo.adicionar_aresta('B', 'C', 2)
grafo.adicionar_aresta('B', 'D', 5)
grafo.adicionar_aresta('C', 'D', 1)
grafo.adicionar_aresta('D', 'E', 3)

origem = 'A'
caminhos = grafo.dijkstra(origem)

for vertice, caminho_para_vertice in caminhos.items():
    print(
        f'Melhor caminho de {origem} para {vertice}: {caminho_para_vertice + [vertice]}, Distância: {distancias[vertice]}')
