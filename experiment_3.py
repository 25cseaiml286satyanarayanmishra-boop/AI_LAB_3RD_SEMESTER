def objective_function(x):
    return -(x**2) + 10 # example function

# HILL CLIMBING FUNCTION
def hill_climbing(start, step_size, max_iteration):
    current = start
    current_value = objective_function(current)

    for i in range(max_iteration):
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        # move to better neighbour
        if left_value > current_value:
            current = left
            current_value = left_value  # Update current value
        elif right_value > current_value:
            current = right
            current_value = right_value  # Update current value
        else:
            break

    return current, current_value

# main program
start = float(input("Enter start point: "))
step_size = float(input("Enter step size: "))
max_iteration = int(input("Enter max iteration: "))

best_position, best_value = hill_climbing(start, step_size, max_iteration)

print("\nbest position =", best_position)
print("max value =", best_value)
