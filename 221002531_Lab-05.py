def take_input():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    graph = [[] for _ in range(vertices)]

    print("Enter each edge in the format 'u v':")
    for _ in range(edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    return graph


def greedy_coloring(graph):
    n = len(graph)
    result = [-1] * n
    result[0] = 0

    for u in range(1, n):
        used = [False] * n
        for i in graph[u]:
            if result[i] != -1:
                used[result[i]] = True
        for color in range(n):
            if not used[color]:
                result[u] = color
                break
    return result


# Main Program
graph = take_input()
coloring = greedy_coloring(graph)

print("\nVertex : Color")
for vertex, color in enumerate(coloring):
    print(f"   {vertex}   :   {color}")
