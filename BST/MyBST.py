from Node import Node

class BSTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None
    
    def insert(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.root = new_node
            return
        
        current = self.root
        parent = None
        while current != None:
            parent = current
            if current.info < info:
                current = current.right
            elif current.info > info:
                current = current.left
            else:
                return

        if info > parent.info:
            parent.right = new_node
        if info < parent.info:
            parent.left = new_node

    def visit(self, p):
        if p != None:
            print(p.info, end=" ")

    def pre_order(self, p):
        if p == None:
            return
        
        self.visit(p)
        self.pre_order(p.left)
        self.pre_order(p.right)

    def in_order(self, p):
        if p == None:
            return
        
        self.in_order(p.left)
        self.visit(p)
        self.in_order(p.right)

    def post_order(self, p):
        if p == None:
            return
        
        self.post_order(p.left)
        self.post_order(p.right)
        self.visit(p)