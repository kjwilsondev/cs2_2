import unittest
from graph import Graph
from vertex import Vertex

class GraphTest(unittest.TestCase):
    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("Abe")
        graph.add_vertex("Max")
        graph.add_vertex("Kyle")

        self.assertEqual(3, graph.get_num_vertices())
        self.assertIsInstance(graph.get_vertex("Abe"), Vertex)


    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("Abe")
        graph.add_vertex("Max")
        graph.add_vertex("Kyle")

        graph.add_edge("Abe", "Max")
        graph.add_edge("Abe", "Kyle", 2)

        self.assertEqual(3, graph.get_num_vertices())
        self.assertEqual(2, graph.get_num_edges())

        graph.add_edge("Kennis", "Kaleb")

        self.assertEqual(5, graph.get_num_vertices())
        self.assertEqual(3, graph.get_num_edges())
        self.assertCountEqual(
            ["Max", "Kyle", "Abe", "Kennis", "Kaleb"],
            graph.get_vertices())

if __name__ == "__main__":
    unittest.main()