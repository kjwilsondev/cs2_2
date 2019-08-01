from graph import Graph

def read_from_file(filename):
    """Read from a file located at `filename` and return the corresponding graph object."""
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # if len(lines) > 0:
    #     lines[0].strip()
    # else:
    #     None

    # Check if it is a graph or directed graph
    g_or_d_str =  lines[0].strip() if len(lines) > 0 else None
    print(lines[0].strip())
    if g_or_d_str != "G" and g_or_d_str != "D":
        raise Exception("File must start with G or D.")
    is_bidirectional = g_or_d_str == "G"

    g = Graph()

    # Add all vertices
    print(lines[1].strip())
    for vertex_key in lines[1].strip("() \n").split(","):
        g.add_vertex(vertex_key)

    # Add all edges
    for line in lines[2:]:
        # Split components of edge
        print(f"line: {line}")
        new_edge = line.strip("() \n").split(",")
        print(f"edge: {new_edge}")
        if len(new_edge) < 2 or len(new_edge) > 3:
            raise Exception("Lines adding edges must include 2 or 3 values")
        
        # Get vertices
        vertex1, vertex2 = new_edge[:2]

        # if len(new_edge) == 3:
        #     int(new_edge[2])
        # else:
        #     None

        # Get weight if it exists
        weight = int(new_edge[2]) if len(new_edge) == 3 else None

        # Add edge(s)
        g.add_edge(vertex1, vertex2, weight)
        if is_bidirectional:
            g.add_edge(vertex2, vertex1, weight)

    return g