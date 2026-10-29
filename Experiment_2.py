def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        # Loop through all adjacent neighbors of the current node
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)

# Main program
graph = {}
n = int(input("Enter the no of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors

start = input("Enter the starting vertex: ")
print("\nGraph:", graph)
print("DFS traversal:", end=" ")

visited = set()
dfs(graph, start, visited)
