import ast

class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.pointers = set()
        
    def points_to(self, pointer):
        self.pointers.add(pointer)

class Graph(object):
    def __init__(self, FILE_PATH = ''):
        pass

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        pass
      
    def add_edge(self, fromVert, toVert, weight = None):
        '''If weight is None: Adds a new, directed edge to the graph that connects two vertices.
        Else: Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        pass
      
    def get_vertex(self, vertKey):
        '''finds the vertex in the graph named vertKey.'''
        pass
      
    def get_vertices(self): 
        '''returns the list of all vertices in the graph.'''
        pass
      
    def get_neighbors(self, x): 
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        pass

content = open("graph_data.txt")
content = (list(content))

# import graph
graph = content[0]
print(graph)

# import vertices
vstring = content[1]
# split vertices by comma
# create array of nodes
vertices = [Vertex(vertix) for vertix in vstring.split(',')]
print(vertices)

# import edges
estring = content[2:]
# take away annoying \n
edges = [edge.strip() for edge in estring]
# convert list of string edges to an array of tuples
# https://stackoverflow.com/questions/25023018/convert-a-string-tuple-to-a-tuple
edges = [ast.literal_eval(edge) for edge in edges]
print(edges)
