from collections import deque

def BFS(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    print("\nBFS Traversal:")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

n = int(input("Enter number of vertices: "))
graph = {}
for i in range(n):
    vertex = input(f"Enter vertex {i+1} : ")
    neighbours = input(f"Enter adjacent vertex of {vertex} (space-separated ): ").split()
    graph[vertex] = neighbours

start = input("Enter the starting vertex: ")
BFS(graph, start)
