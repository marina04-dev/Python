class Node:
    def __init__(self, descr="", neighbors=""):
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
            self.neighbors = []
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
        
    def __str__(self):
        st = ""
        for node in self.nodes:
            st += f"\n{node.descr}: "
            for neighbor in node.neighbors:
                st += f" {neighbor.descr}"
                
        return st
        
        
def main():
    facebookUsers = Graph()
    for user in ["Bob", "Anne", "Elisa", "Diana", "Carl"]:
        facebookUsers.add_vertex(user)
        
    facebookUsers.add_edge("Carl", "Bob")
    facebookUsers.add_edge("Carl", "Elisa")
    facebookUsers.add_edge("Carl", "Diana")
    
    facebookUsers.add_edge("Diana", "Bob")
    facebookUsers.add_edge("Diana", "Anne")
    
    facebookUsers.add_edge("Elisa", "Anne")
    
    facebookUsers.add_edge("Anne", "Bob")
    
    print(facebookUsers)
    
main()
