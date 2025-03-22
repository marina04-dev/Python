class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, elem):
        self.array.append(elem)

    def dequeue(self):
        if not self.array:
            return None
        else:
            return self.array.pop(0)

    def __str__(self):
        return ", ".join(self.array)

    def __add__(self, other):
        new_q = Queue()
        new_q.array = self.array[:]
        new_q.enqueue(other)
        return new_q

    def __iadd__(self, other):
        self.enqueue(other)
        return self

    def __neg__(self):
        return self.dequeue()

    def __len__(self):
        return len(self.array)

class Node:
    def __init__(self, descr="", neighbors=None):
        self.descr = descr
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors


class Graph:
    def __init__(self):
        self.nodes = []

    def add_vertex(self, descr="", neighbors=None):
        if neighbors is None:
            neighbors = []
        self.nodes += [Node(descr, neighbors)]

    def __index_of(self, descr):
        for i in range(len(self.nodes)):
            if descr == self.nodes[i].descr:
                return i

    def add_edge(self, descr1, descr2):
        index1 = self.__index_of(descr1)
        index2 = self.__index_of(descr2)
        self.nodes[index1].neighbors += [self.nodes[index2]]
        self.nodes[index2].neighbors += [self.nodes[index1]]

    def neighbors(self, descr):
        return self.nodes[self.__index_of(descr)].neighbors

    def __str__(self):
        st = ""
        for node in self.nodes:
            st += f"\n{node.descr}: "
            for neighbor in node.neighbors:
                st += f" {neighbor.descr}"

        return st    
        
        
        
def breadth_first_search(graph, start, finish):
    q = Queue()
    discovered = [start]
    q.enqueue(start)
    parent = {}
    while len(q) > 0:
        v = q.dequeue()
        if v == finish:
            break
        for neighbor in graph.neighbors(v):
            if neighbor.descr not in discovered:
                discovered += [neighbor.descr]
                parent[neighbor.descr] = v
                q.enqueue(neighbor.descr)

    path = [finish]
    while path[0] != start:
        path = [parent[path[0]]] + path

    print(path)


def main():
    facebook_users = Graph()
    for user in ["Bob", "Anne", "Elisa", "Diana", "Carl"]:
        facebook_users.add_vertex(user)

    facebook_users.add_edge("Carl", "Bob")
    facebook_users.add_edge("Carl", "Elisa")
    facebook_users.add_edge("Carl", "Diana")
    facebook_users.add_edge("Diana", "Bob")
    facebook_users.add_edge("Diana", "Anne")
    facebook_users.add_edge("Elisa", "Anne")
    facebook_users.add_edge("Anne", "Bob")
    print(facebook_users)
    print("\n")
    breadth_first_search(facebook_users, "Carl", "Anne")


main()
