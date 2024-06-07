class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, sourcevertex, destinationvertex):
        if sourcevertex in self.adjacency_list and destinationvertex in self.adjacency_list:
            self.adjacency_list[sourcevertex].append(destinationvertex)
            return True
        return False

    def delete_edge(self, sourcevertex, destinationvertex):
        if sourcevertex in self.adjacency_list and destinationvertex in self.adjacency_list:
            self.adjacency_list[sourcevertex].remove(destinationvertex)
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, " : ", self.adjacency_list[vertex])

    def delete_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            del self.adjacency_list[vertex]
            for vertices in self.adjacency_list.values():
                if vertex in vertices:
                    vertices.remove(vertex)
            return True
        return False


customgraph = Graph()
customgraph.add_vertex("A")
customgraph.add_vertex("B")
customgraph.add_vertex("C")
customgraph.add_vertex("D")
customgraph.add_vertex("E")
customgraph.add_edge("A", "B")
customgraph.add_edge("A", "C")
customgraph.add_edge("C", "A")
customgraph.add_edge("C", "E")
customgraph.add_edge("A", "D")
customgraph.add_edge("D", "A")
customgraph.add_edge("B", "D")
customgraph.add_edge("E", "C")
customgraph.add_edge("D", "E")
customgraph.print_graph()
# customgraph.delete_edge("A","D")
print("despues de Eliminar A D")
print("\n")
customgraph.print_graph()
customgraph.delete_vertex("A")
print("despues de Eliminar vertex A")
print("\n")
customgraph.print_graph()
