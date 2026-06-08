from Node import Node
from My_Queue import Queue

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

    def breadth(self):
        if self.root == None:
            return
        
        q = Queue()
        q.enqueue(self.root)
        while not q.isEmpty():
            p = q.dequeue()

            if p.left != None:
                q.enqueue(p.left)
            if p.right != None:
                q.enqueue(p.right)

            self.visit(p)

    def search(self, x):
        current = self.root

        while current != None:
            if x == current.info:
                return current

            if x > current.info:
                current = current.right
            else:
                current = current.left

        return None
    
    def searchNodeHavingOnlyLeftChildByPreOrder(self, p):
        if p == None:
            return None

        # visit
        if p.left != None and p.right == None:
            return p

        # left
        found = self.searchNodeHavingOnlyLeftChildByPreOrder(p.left)
        if found != None:
            return found

        # right
        return self.searchNodeHavingOnlyLeftChildByPreOrder(p.right)
    
    def searchNodeHavingOnlyRightChildByPostOrder(self, p):
        if p == None:
            return None
        
        found = self.searchNodeHavingOnlyRightChildByPostOrder(p.left)
        if found != None:
            return found
        
        found = self.searchNodeHavingOnlyRightChildByPostOrder(p.right)
        if found != None:
            return found
    
        if p.left == None and p.right != None:
            return p
        
        return None
    
    def searchBothChildrenByInOrder(self, p):
        if p == None:
            return None

        found = self.searchBothChildrenByInOrder(p.left)
        if found != None:
            return found

        if p.left != None and p.right != None:
            return p

        return self.searchBothChildrenByInOrder(p.right)
    
    def searchLeafByBreadth(self):
        if self.root == None:
            return None

        q = Queue()
        q.enqueue(self.root)

        while not q.isEmpty():
            p = q.dequeue()

            if p.left == None and p.right == None:
                return p

            if p.left != None:
                q.enqueue(p.left)

            if p.right != None:
                q.enqueue(p.right)

        return None