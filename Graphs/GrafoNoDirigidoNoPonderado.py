class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    def delete_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for key in self.adjacency_list:
                self.adjacency_list[key] = [i for i in self.adjacency_list[key] if i != vertex]
            del self.adjacency_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")


customgraph = Graph()
customgraph.add_vertex("A")
customgraph.add_vertex("B")
customgraph.add_vertex("C")
customgraph.add_vertex("D")
customgraph.add_vertex("E")
customgraph.add_edge("A", "B")
customgraph.add_edge("A", "C")
customgraph.add_edge("A", "D")
customgraph.add_edge("B", "D")
customgraph.add_edge("C", "E")
customgraph.add_edge("D", "E")
customgraph.print_graph()
# print("After deleting edge")
# customgraph.delete_edge("A", "D")
# customgraph.print_graph()
print("----------------------------------------------")
customgraph.delete_vertex("A")
customgraph.print_graph()

