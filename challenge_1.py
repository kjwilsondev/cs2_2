import ast

class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        # check if vertex is already a neighbor
        if vertex in self.neighbors:
            return
        # if not, add vertex to neighbors and assign weight.
        self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # return the neighbors
        return self.neighbors

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # return the weight of the edge from this
        # vertex to the given vertex.
        try:
            return self.neighbors[vertex]
        except:
            raise ValueError("no weight found")


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # increment the number of vertices
        self.numVertices += 1
        # create a new vertex
        new_vertex = Vertex(key)
        # add the new vertex to the vertex list
        self.vertList[key] = new_vertex
        # return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        try:
            return self.vertList[key]
        except:
            raise KeyError("no vertex found")

    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""
        # if either vertex is not in the graph,
        if key1 not in self.vertList:
            self.add_vertex(key1)
        if key2 not in self.vertList:
            self.add_vertex(key2)
        # if both vertices in the graph, add the
        # edge by making key1 a neighbor of key2
        self.vertList[key1].add_neighbor(self.vertList[key2], weight)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))


# OLD TEST CODE

# content = open("graph_data.txt")
# content = (list(content))

# # import graph
# graph = content[0]
# print(graph)

# # import vertices
# vstring = content[1]
# # split vertices by comma
# # create array of nodes
# vertices = [Vertex(vertix) for vertix in vstring.split(',')]
# print(vertices)

# # import edges
# estring = content[2:]
# # take away annoying \n
# edges = [edge.strip() for edge in estring]
# # convert list of string edges to an array of tuples
# # https://stackoverflow.com/questions/25023018/convert-a-string-tuple-to-a-tuple
# edges = [ast.literal_eval(edge) for edge in edges]
# print(edges)
