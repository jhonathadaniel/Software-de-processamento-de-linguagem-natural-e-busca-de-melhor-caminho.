import unittest
from unittest.mock import patch
from Dijkistra import Dijkistra

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        grafo = Dijkistra()
        grafo.adicionar_aresta('A', 'B', 1)
        grafo.adicionar_aresta('A', 'C', 4)
        grafo.adicionar_aresta('B', 'C', 2)
        grafo.adicionar_aresta('B', 'D', 5)
        grafo.adicionar_aresta('C', 'D', 1)
        grafo.adicionar_aresta('D', 'E', 3)

        origem = 'A'

        with patch('heapq.heappop', side_effect=lambda x: x.pop(0)):
            caminhos, distancias = grafo.dijkstra(origem)

        expected_caminhos = {
            'A': [],
            'B': ['A', 'B'],
            'C': ['A', 'B', 'C'],
            'D': ['A', 'B', 'C', 'D'],
            'E': ['A', 'B', 'C', 'D', 'E']
        }

        expected_distancias = {
            'A': 0,
            'B': 1,
            'C': 3,
            'D': 4,
            'E': 7
        }

        for vertice, caminho_para_vertice in caminhos.items():
            self.assertTrue(all(v in expected_caminhos[vertice] for v in caminho_para_vertice))

        self.assertEqual(distancias, expected_distancias)

if __name__ == '__main__':
    unittest.main()
