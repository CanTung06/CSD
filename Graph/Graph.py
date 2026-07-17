from Stack import *
class Graph:
    def __init__(self, data):
        self.a = data

    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end=" ")
            print("")
        print("")

    def visit(self, i):
        print(f"{chr(i+65)}", end=" ")

    def depth_first(self, start):
        visited = [False]*len(self.a)
        visited[start] = True
        self.depth(start, visited)
        for i in range(len(visited)):
            if not visited[i]:
                visited[i] = True
                self.depth(i, visited)

    def depth(self, start, visited):
        self.visit(start)
        for i in range(len(visited)):
            if self.a[start][i] != 0 and not visited[i]:
                visited[i] = True
                self.depth(i, visited)

    def breadth_first(self, start):
        visited = [False]*len(self.a)
        self.breadth(start, visited)
        for i in range(len(self.a)):
            if not visited[i]:
                self.breadth(i, visited)

    def breadth(self, start, visited):
        q = []
        q.append(start)
        visited[start] = True
        while len(q) > 0:
            h = q.pop(0)
            self.visit(h)
            for i in range(len(self.a)):
                if self.a[h][i] > 0 and not visited[i]:
                    visited[i] = True
                    q.append(i)

    def dijkstra(self, start, end):
        n = len(self.a)
        INF = float('inf')

        dist = [INF] * n
        visited = [False] * n
        parent = [-1] * n

        dist[start] = 0

        while True:
            u = -1
            min_dist = INF

            # Tìm đỉnh chưa xét có khoảng cách nhỏ nhất
            for i in range(n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            # Không còn đường đi
            if u == -1:
                break

            visited[u] = True

            # Đến đích thì dừng
            if u == end:
                break

            # Cập nhật khoảng cách
            for v in range(n):
                if self.a[u][v] != 0 and not visited[v]:
                    if dist[u] + self.a[u][v] < dist[v]:
                        dist[v] = dist[u] + self.a[u][v]
                        parent[v] = u

        # Không có đường đi
        if dist[end] == INF:
            print("No path")
            return

        # Truy vết đường đi
        path = []
        cur = end
        while cur != -1:
            path.append(chr(cur + 65))
            cur = parent[cur]

        path.reverse()

        print("Shortest path:", " -> ".join(path))
        print("Distance:", dist[end])

    def degree(self, v):
        deg = 0
        for i in range(len(self.a)):
            if self.a[v][i] != 0:
                deg += 1
        return deg
    
    def euler(self, start):
        n = len(self.a)

        # Copy ma trận
        b = [row[:] for row in self.a]

        st = Stack()
        eu = []

        st.push(start)

        while not st.isEmpty():
            r = st.top()

            found = False
            for i in range(n):
                if b[r][i] > 0:
                    st.push(i)
                    b[r][i] = 0
                    b[i][r] = 0
                    found = True
                    break

            if not found:
                eu.append(st.pop())

        eu.reverse()

        for x in eu:
            self.visit(x)

    def hamilton(self, start):
        n = len(self.a)

        visited = [False] * n
        path = []

        def Try(v):
            path.append(v)
            visited[v] = True

            if len(path) == n:
                if self.a[v][start] != 0:
                    path.append(start)

                    for x in path:
                        self.visit(x)

                    return True

            for i in range(n):
                if self.a[v][i] != 0 and not visited[i]:
                    if Try(i):
                        return True

            visited[v] = False
            path.pop()
            return False

        Try(start)