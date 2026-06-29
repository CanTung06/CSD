from Graph import *
class Main:
    def __init__(self):
        self.data = []

    def gen_data1(self):
        self.data = [
            #[a, b, c, d, e, f, g, h, i]
            [0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0]
        ]

m = Main()
m.gen_data1()
g = Graph(m.data)
g.display()
print("Depth First Traverse: ")
g.depth_first(0)
print()
print("Breadth First Traverse: ")
g.breadth_first(0)
print()
g.dijkstra(0, 3)