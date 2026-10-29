# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values for each node
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        # Find the node in open_list with the lowest f_cost (g_cost + heuristic)
        current = min(open_list, key=lambda x: x[1] + heuristic[x[0]])
        open_list.remove(current)
        current_node = current[0]
        
        if current_node == goal:
            path = [goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_cost[goal]
            
        for neighbor, weight in graph.get(current_node, []):
            new_cost = g_cost[current_node] + weight
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                open_list.append((neighbor, new_cost))
                
    return None, float('inf')

# MAIN PROGRAM
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

path, cost = astar(start, goal)

if path:
    print("Shortest Path:")
    print(" -> ".join(path))
    print("total cost:", cost)
else:
    print("path not found")

print("Result: We have successfully implemented A* Algorithm using Python.")
