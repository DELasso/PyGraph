class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)


class queue:

    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.queue]
        return ' '.join(result)

    def is_empty(self):
        return self.linkedlist.head == None

    def enqueue(self, e):
        new_node = Node(e)
        if self.linkedlist.head == None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            new_node.next = None
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "No hay elementos en la lista"
        else:
            popped_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            popped_node.next = None
            return popped_node.value


class stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.linkedlist]
        return ' '.join(result)

    def is_empty(self):
        return self.linkedlist.head == None

    def push(self, e):
        new_node = Node(e)
        if self.linkedlist.head == None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            new_node.next = self.linkedlist.head
            self.linkedlist.head = new_node

    def pop(self):

        if self.linkedlist.head == None:
            return None

        popped_node = self.linkedlist.head
        self.linkedlist.head = self.linkedlist.head.next
        popped_node.next = None
        return popped_node.value


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def print_graph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex, " : ", self.adjacency_list[vertex])

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

    # Dado un grafo dirigido y dos nodos (S y E), diseñe un algoritmo para averiguar si existe una ruta de S a E.
    def route_exist(self, sourcevertex, destinationvertex):

        customqueue = queue()
        visited = set()

        customqueue.enqueue(sourcevertex)
        visited.add(sourcevertex)

        while not customqueue.is_empty():

            current_vertex = customqueue.dequeue()

            if current_vertex == destinationvertex:
                return True

            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    visited.add(adjacency_vertex)
                    customqueue.enqueue(adjacency_vertex)

        return False

    # Dado un grafo dirigido y dos nodos (S y E), diseñe un algoritmo que retorne cuantas rutas existen de S a E.
    def route_count(self, sourcevertex, destinationvertex):

        customstack = stack()
        visited = set()

        customstack.push(sourcevertex)
        count_route = 0

        while not customstack.is_empty():
            current_vertex = customstack.pop()

            if current_vertex == destinationvertex:
                count_route += 1

            if current_vertex not in visited:
                visited.add(current_vertex)

            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    customstack.push(adjacency_vertex)
                elif adjacency_vertex == destinationvertex:
                    customstack.push(adjacency_vertex)

        return count_route

    # Dado un grafo dirigido escriba una función que identifique si hay ciclos en él. Un ciclo es una secuencia de
    # vértices conectados por aristas, donde el vértice inicial y final son el mismo.

    def has_cycle(self):

        for vertex in self.adjacency_list.keys():
            visited = set()
            if self.cycle_helper(vertex, visited):
                print("vertice con ciclo", vertex)
                return True
        return False

    def cycle_helper(self, vertex, visited):

        customstack = stack()
        customstack.push((vertex, None))

        while not customstack.is_empty():
            current_vertex, parent = customstack.pop()
            if current_vertex in visited and current_vertex == vertex:
                return True
            visited.add(current_vertex)
            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex != parent and adjacency_vertex not in visited:
                    customstack.push((adjacency_vertex, current_vertex))
                elif adjacency_vertex != parent and adjacency_vertex == vertex:
                    customstack.push((adjacency_vertex, current_vertex))

        return False

    # Dado un grafo escriba una función que determine si es un árbol o no. Un árbol es un grafo no dirigido y
    # conexo que no tiene ciclos.

    def is_tree(self):
        for vertex in self.adjacency_list.keys():
            visited = set()
            if self.is_tree_helper(vertex, visited, None):
                return False
        return True

    def is_tree_helper(self, vertex, visited, parent):
        visited.add(vertex)
        for adjacency_vertex in self.adjacency_list[vertex]:
            if adjacency_vertex not in visited:
                if self.is_tree_helper(adjacency_vertex, visited, vertex):
                    return True
            elif adjacency_vertex != parent:
                return True
        return False

    # Dado un grafo no dirigido, escribe una función para representar el grafo usando: Matriz de adyacencia

    def adjacency_matrix(self):
        vertices = list(self.adjacency_list.keys())
        vertices.sort()
        matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        for i in range(len(vertices)):
            for adjacency_vertex in self.adjacency_list[vertices[i]]:
                j = vertices.index(adjacency_vertex)
                matrix[i][j] = 1
        return matrix

    # Escribe un programa que cuente el número de componentes conexos en un grafo no dirigido.

    def connected_components(self):
        visited = set()
        count = 0
        for vertex in self.adjacency_list.keys():
            if self.connected_components_helper(vertex, visited):
                count += 1
        return count

    # Escribe un programa que cuente el número de componentes conexos en un grafo no dirigido.
    def connected_components_helper(self, vertex, visited):
        if vertex in visited:
            return False
        visited.add(vertex)
        for adjacency_vertex in self.adjacency_list[vertex]:
            self.connected_components_helper(adjacency_vertex, visited)
        return True

    # Implementa un método para encontrar el camino más corto entre dos nodos en un grafo no ponderado usando BFS E
    # Ir imprimiendo por donde va el camino.

    def shortest_path(self, sourcevertex, destinationvertex):
        customqueue = queue()
        visited = set()
        distance = {}

        customqueue.enqueue(sourcevertex)
        visited.add(sourcevertex)
        distance[sourcevertex] = 0

        while not customqueue.is_empty():
            current_vertex = customqueue.dequeue()
            if current_vertex == destinationvertex:
                return distance[destinationvertex]

            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    visited.add(adjacency_vertex)
                    customqueue.enqueue(adjacency_vertex)
                    distance[adjacency_vertex] = distance[current_vertex] + 1
        return -1


customgraph = Graph()
customgraph.add_vertex("A")
customgraph.add_vertex("B")
customgraph.add_vertex("C")
customgraph.add_vertex("D")
customgraph.add_vertex("E")
customgraph.add_vertex("F")
customgraph.add_vertex("G")
"""
customgraph.add_edge("A", "B")
customgraph.add_edge("A", "C")
customgraph.add_edge("B", "C")
customgraph.add_edge("D", "E")
customgraph.add_edge("F", "G")



customgraph.add_edge("A", "B")
customgraph.add_edge("A", "C")
customgraph.add_edge("B", "G")
customgraph.add_edge("C", "D")
customgraph.add_edge("C", "E")
customgraph.add_edge("D", "C")
customgraph.add_edge("D", "G")
customgraph.add_edge("D", "F")
customgraph.add_edge("E", "F")
customgraph.add_edge("F", "D")
"""

customgraph.add_edge("A", "B")
customgraph.add_edge("A", "C")
customgraph.add_edge("B", "D")
customgraph.add_edge("B", "E")
customgraph.add_edge("C", "F")
customgraph.add_edge("C", "G")
customgraph.add_edge("G", "C")


customgraph.print_graph()
print(customgraph.adjacency_matrix())


