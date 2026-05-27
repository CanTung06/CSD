from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Kiểm tra queue rỗng
    def isEmpty(self):
        return self.front is None

    # Thêm phần tử vào cuối queue
    def enqueue(self, x):
        newNode = Node(x, None)

        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    # Lấy và xóa phần tử đầu queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue rong")
            return None

        data = self.front.info
        self.front = self.front.next

        # Nếu queue rỗng sau khi xóa
        if self.front is None:
            self.rear = None

        return data

    # Xem phần tử đầu
    def peek(self):
        if self.isEmpty():
            return None
        return self.front.info

    # Hiển thị queue
    def display(self):
        if self.isEmpty():
            print("Queue rong")
            return

        p = self.front
        while p:
            print(p.info, end=" <- ")
            p = p.next
        print("None")