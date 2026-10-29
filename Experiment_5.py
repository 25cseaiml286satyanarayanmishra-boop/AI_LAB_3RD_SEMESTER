# Min-Max Algorithm
def minmax(depth, nodeindex, ismax, scores, height):
    # Base case: leaf nodes reached
    if depth == height:
        return scores[nodeindex]

    if ismax:
        return max(minmax(depth+1, nodeindex*2, False, scores, height),
                   minmax(depth+1, nodeindex*2+1, False, scores, height))
    else:
        return min(minmax(depth+1, nodeindex*2, True, scores, height),
                   minmax(depth+1, nodeindex*2+1, True, scores, height))

# Main program
scores = list(map(int, input("Enter 8 node values separated by spaces: ").split()))
height = 3
result = minmax(0, 0, True, scores, height)
print("\nThe optimal value is:", result)
