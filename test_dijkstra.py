import unittest
from unittest.mock import patch
import heapq
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

        with patch.object(heapq, 'heappop') as mock_heappop, \
             patch.object(heapq, 'heappush') as mock_heappush:
            mock_heappop.side_effect = [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
            mock_heappush.side_effect = None

            caminhos = grafo.dijkstra('A')

        expected_caminhos = {
            'A': [],
            'B': ['A', 'B'],
            'C': ['A', 'C'],
            'D': ['A', 'C', 'D'],
            'E': ['A', 'C', 'D', 'E']
        }

        self.assertEqual(caminhos, expected_caminhos)

if __name__ == '__main__':
    unittest.main()
