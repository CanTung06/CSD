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
    
    def delete(self, info):
        current = self.root
        parent = None

        while current != None and current.info != info:
            parent = current
            if info < current.info:
                current = current.left
            if info > current.info:
                current = current.right

        if current == None:
            return
        
        if current.left == None and current.right == None:
            if self.root.info == info:
                self.root = None
                return
            if info < parent.info:
                parent.left = None
            if info > parent.info:
                parent.right = None

            return
        
        # Xoa Node co duy nhat 1 con ben trai
        if current.left != None and current.right == None:
            if self.root.info == info:
                self.root = current.left
                return
            if info < parent.info:
                parent.left = current.left
                current.left = None
            if info > parent.info:
                parent.right = current.left
                current.left = None
            
            return

        # Xoa Node co duy nhat 1 con ben phai
        if current.left == None and current.right != None:
            if self.root.info == info:
                self.root = current.right
                return
            if info < parent.info:
                parent.left = current.right
                current.right = None
            if info > parent.info:
                parent.right = current.right
                current.right = None
            
            return
        
        # Xoa Node co 2 con (delete by copying)
        if current.left != None and current.right != None:
            most_right = current.left
            parent_mostRight = None

            while most_right.right != None:
                parent_mostRight = most_right
                most_right = most_right.right
            
            current.info = most_right.info # Copy info cua most_right cho current
            
            if parent_mostRight == None:
                current.left = most_right.left
            else:
                parent_mostRight.right = most_right.left

            most_right.left = None

    def delete_by_merging(self, info):
        current = self.root
        parent = None

        while current != None and current.info != info:
            parent = current
            if info < current.info:
                current = current.left
            if info > current.info:
                current = current.right

        if current == None:
            return

        # Xoa node la
        if current.left == None and current.right == None:
            if self.root.info == info:
                self.root = None
                return

            if info < parent.info:
                parent.left = None

            if info > parent.info:
                parent.right = None

            return

        # Xoa node chi co con trai
        if current.left != None and current.right == None:
            if self.root.info == info:
                self.root = current.left
                return

            if info < parent.info:
                parent.left = current.left
                current.left = None

            if info > parent.info:
                parent.right = current.left
                current.left = None

            return

        # Xoa node chi co con phai
        if current.left == None and current.right != None:
            if self.root.info == info:
                self.root = current.right
                return

            if info < parent.info:
                parent.left = current.right
                current.right = None

            if info > parent.info:
                parent.right = current.right
                current.right = None

            return

        # Xoa node co 2 con (delete by merging)
        if current.left != None and current.right != None:
            left_tree = current.left

            # Tim node phai nhat cua cay con trai
            most_right = left_tree
            while most_right.right != None:
                most_right = most_right.right

            # Ghep cay con phai vao node phai nhat
            most_right.right = current.right

            # Neu current la root
            if self.root == current:
                self.root = left_tree
                return

            # Noi parent voi cay da merge
            if info < parent.info:
                parent.left = left_tree
            else:
                parent.right = left_tree

    def rotate_right(self, info):
        grand = None
        parent = self.root

        while parent != None and parent.info != info:
            grand = parent
            if info < parent.info:
                parent = parent.left
            if info > parent.info:
                parent = parent.right

        if parent == None or parent.left == None:
            return
        
        left_child = parent.left
        right_grand_child = left_child.right
        
        if grand == None:
            self.root = left_child
        else:
            if parent.info > grand.info:
                grand.right = left_child
            if parent.info < grand.info:
                grand.left = left_child

        left_child.right = parent
        parent.left = right_grand_child