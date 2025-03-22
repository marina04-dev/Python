class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 
        
        
class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def insert_root(self, data):
        n = Node(data)
        self.root = n
        
    def insert_left(self, node, data):
        n = Node(data)
        node.left = n 
        
    def insert_right(self, node, data):
        n = Node(data)
        node.right = n 
        
    def __str__(self):
        st = ""
        def rec_str(n):
            nonlocal st 
            if n is None:
                st += "_"
            else:
                st += str(n.data)
                st += "("
                rec_str(n.left)
                st += ","
                rec_str(n.right)
                st += ")"
        rec_str(self.root)
        return st 
            
     
class BinarySearchTree(Tree):
    def __init__(self):
        super().__init__()
        
    def insert(self, data):
        if self.root is None:
            self.insert_root(data)
            print(str(data) + " Inserted!")
            
        node = self.root 
        while True:
            if data == node.data:
                print(str(data) + " Is Already Been Inserted Before!")
                break 
            elif data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    print(str(data) + " Inserted!")
                    break 
                else:
                    node = node.left 
            else:
                if node.right is None:
                    node.right = Node(data)
                    print(str(data) + " Inserted!")
                    break 
                else:
                    node = node.right 
    
    def inorder(self):
        ret_list = []
        def rec_inorder(node):
            nonlocal ret_list
            if node is not None:
                rec_inorder(node.left)
                ret_list += (node.data)
                rec_inorder(node.right)
        rec_inorder(self.root)
        return ret_list
            
t = Tree()
t.insert_root("A")
t.insert_left(t.root, "B")
t.insert_right(t.root, "C")
t.insert_left(t.root.left, "D")
t.insert_right(t.root.left, "E")
t.insert_right(t.root.right, "F")
print(t)

t2 = BinarySearchTree()
t2.insert(2)
t2.insert(5)
t2.insert(8)
t2.insert(11)
t2.insert(7)
print(t2)
print(t2.inorder())
