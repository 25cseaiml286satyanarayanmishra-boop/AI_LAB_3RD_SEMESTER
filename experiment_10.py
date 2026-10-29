from itertools import permutations

# function to solve ISP
def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_cost = float('inf')
    best_path = None

    # generate all possible tours
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start

        for city in perm:
            current_path.append(city)
            current_cost += graph[k][city]  # FIXED: Changed start to k
            k = city

        current_cost += graph[k][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost

# main program
n = int(input("enter the number of cities:"))
print("enter the cost matrix")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("enter the starting city 0 to ():"))
best_path, min_cost = travelling_salesman(graph, start)

print("the best path is", best_path)
print("the minimum cost is", min_cost)
