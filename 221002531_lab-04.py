from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.visited = [False] * self.V
        self.result = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, depth_limit):
        if depth_limit == 0:
            return
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, depth_limit - 1)
        self.result.append(node)

    def iddfs(self, max_depth):
        for depth in range(1, max_depth + 1):
            self.visited = [False] * self.V
            self.result = []
            for i in range(self.V):
                if not self.visited[i]:
                    self.dfs(i, depth)
            if len(self.result) == self.V:
                break
        return self.result[::-1]

# -------- User Input Section --------
print("Enter number of vertices:")
V = int(input())

g = Graph(V)

print("Enter number of edges:")
E = int(input())

print("Enter the edges in format 'u v' (from node u to node v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

# -------- Output Section --------
print("\nTopological Order using IDDFS:")
topo_order = g.iddfs(V)
print(topo_order)
