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

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, " : ", self.adjacency_list[vertex])

    def delete_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for adjacency_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[adjacency_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def bfs(self, vertex):
        visited = set()
        customqueue = queue()
        customqueue.enqueue(vertex)
        visited.add(vertex)
        while not customqueue.is_empty():
            current_vertex = customqueue.dequeue()
            print(current_vertex, end=" ")
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    customqueue.enqueue(adjacent_vertex)
                    visited.add(adjacent_vertex)

    def dfs(self, vertex):
        visited = set()
        customstack = stack()
        customstack.push(vertex)
        visited.add(vertex)
        while not customstack.is_empty():
            current_vertex = customstack.pop()
            print(current_vertex, end=" ")
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    customstack.push(adjacent_vertex)
                    visited.add(adjacent_vertex)

customgraph = Graph()
"""
customgraph.add_vertex("A")
customgraph.add_vertex("B")
customgraph.add_vertex("C")
customgraph.add_vertex("D")
customgraph.add_vertex("E")
customgraph.add_edge("A","B")
customgraph.add_edge("A","C")
customgraph.add_edge("A","D")
customgraph.add_edge("B","D")
customgraph.add_edge("C","E")
customgraph.add_edge("D","E")
"""
customgraph.add_vertex("A")
customgraph.add_vertex("B")
customgraph.add_vertex("C")
customgraph.add_vertex("D")
customgraph.add_edge("A", "B")
customgraph.add_edge("A", "C")
customgraph.add_edge("B", "D")
customgraph.add_edge("C", "D")

customgraph.print_graph()
print("\n")
#customgraph.print_graph()
print("BFS")
customgraph.bfs("A")
print("\n") 
print("DFS")
customgraph.dfs("A")