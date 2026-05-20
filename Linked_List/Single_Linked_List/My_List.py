from Node import Node

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return (self.head == None)
    
    def clear(self):
        self.head = None
        self.tail = None

    def addLast(self, new_info):
        new_node = Node(new_info, None)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def visit(self, node):
        print(node.info, end=" -> ")

    def traverse(self):
        current = self.head
        while current != None:
            self.visit(current)
            current = current.next
        print(None)

    def addFirst(self, new_info):
        new_node = Node(new_info, None)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def getFirst(self):
        if self.isEmpty():
            return None
        
        return self.head.info
    
    def getLast(self):
        if self.isEmpty():
            return None
        
        return self.tail.info
    
    def removeFisrt(self):
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            
            temp = self.head.next
            self.head.next = None
            self.head = temp

    def removeLast(self):
        if not self.isEmpty():
            current = self.head
            while current.next != self.tail:
                current = current.next
                
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            
            current.next = None
            self.tail = current

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count
    
    def getAt(self, index):
        current = self.head
        count = 0
        while current != None:
            if count == index:
                return current.info
            
            count += 1
            current = current.next

    def indexOf(self, info):
        current = self.head
        index = 0
        while current != None:
            if current.info == info:
                return index
            index += 1
            current = current.next

        return -1
    
    def addAt(self, index, info):
        new_node = Node(info, None)
        current = self.head
        pre_index = None
        count = 0

        if index == 0 or self.isEmpty():
            self.addFirst(info)
            return
        if index == self.size():
            self.addLast(info)
            return

        while current != None:
            if count == index - 1:
                pre_index = current
                break

            count += 1
            current = current.next
        
        new_node.next = pre_index.next
        pre_index.next = new_node

    def removeAt(self, index):
        if index == 0:
            self.removeFisrt()
            return
        if index == self.size() - 1:
            self.removeLast()
            return
        if self.isEmpty() or (index < 0 or index >= self.size()):
            return

        pre_remove_node = self.head
        count = 0

        while count < index - 1:
            pre_remove_node = pre_remove_node.next
            count += 1

        remove_node = pre_remove_node.next
        pre_remove_node.next = remove_node.next
        remove_node.next = None

    def sort(self):
        i = self.head
        while i != self.tail:
            j = i.next
            while j != None:
                if i.info > j.info:
                    temp = i.info
                    i.info = j.info
                    j.info = temp
                j = j.next
            i = i.next

    def sort_from_to(self, from_index, to_index):
        if self.head is None or from_index < 0 or to_index < 0 or from_index >= to_index:
            return
        
        current_node = self.head
        current_index = 0
        to_node = None
        from_node = None

        while current_index < from_index and current_node is not None:
            current_node = current_node.next
            current_index += 1
        from_node = current_node

        while current_index < to_index and current_node is not None:
            current_node = current_node.next
            current_index += 1
        to_node = current_node

        if from_node is None or to_node is None:
            return
        
        i = from_node
        while i != to_node:
            j = i.next
            while j != to_node.next:
                if i.info > j.info:
                    temp = i.info
                    i.info = j.info
                    j.info = temp
                j = j.next
            i = i.next

    def reverse(self):
        prev = None
        current = self.head
        

        while current != None:
            after = current.next
            current.next = prev

            prev = current
            current = after

        self.tail = self.head
        self.head = prev