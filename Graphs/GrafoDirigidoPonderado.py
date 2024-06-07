class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
            return True
        return False

    def add_edge(self, sourcevertex, destinationvertex, weight):
        if sourcevertex in self.adjacency_list and destinationvertex in self.adjacency_list:
            self.adjacency_list[sourcevertex][destinationvertex] = weight
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
customgraph.add_edge("A", "B", 10)
customgraph.add_edge("A", "C", 4)
customgraph.add_edge("C", "A", 8)
customgraph.add_edge("C", "E", 12)
customgraph.add_edge("A", "D", 5)
customgraph.add_edge("D", "A", 9)
customgraph.add_edge("B", "D", 7)
customgraph.add_edge("E", "C", 4)
customgraph.add_edge("D", "E", 15)
customgraph.print_graph()
# customgraph.delete_edge("A","D")
print("despues de Eliminar A D")
print("\n")
# customgraph.print_graph()
# customgraph.delete_vertex("A")
print("despues de Eliminar vertex A")
print("\n")
customgraph.print_graph()
