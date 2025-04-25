import random

# Directions for the robot to move: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))


# DFS to perform topological sort
def dfs(grid, row, col, visited, stack):
    if visited[row][col]:
        return

    visited[row][col] = True

    # Explore the four directions (up, down, left, right)
    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]

        # Check if the new position is within bounds and has not been visited
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and not visited[new_row][new_col]:
            dfs(grid, new_row, new_col, visited, stack)

    # Push current node to the stack (this will be the topological order)
    stack.append((row, col))


# Function to find the topological order starting from the top-left corner
def find_topological_order(N):
    # Create a grid with 0's representing unvisited nodes
    grid = [[0 for _ in range(N)] for _ in range(N)]

    # Initialize visited array to keep track of visited nodes
    visited = [[False for _ in range(N)] for _ in range(N)]

    stack = []

    # Start DFS traversal from (0,0) and generate the topological order
    dfs(grid, 0, 0, visited, stack)

    # Reverse the stack to get the correct topological order
    topological_order = stack[::-1]

    return topological_order


def main():
    N = int(input("Enter grid size (N): "))

    # Find the topological order of nodes
    topological_order = find_topological_order(N)

    # Print the topological order
    print("\nTopological Order of Node Traversal:")
    for node in topological_order:
        print(node)


if __name__ == "__main__":
    main()
