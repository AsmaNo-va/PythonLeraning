from collections import deque

class Node:
    def __init__(self, x, y, level, parent=None):
        self.x = x  # x-coordinate of the node
        self.y = y  # y-coordinate of the node
        self.level = level  # Number of moves from the source
        self.parent = parent  # Stores parent node for path tracking

class BFSPathFinder:
    def __init__(self):
        # Directions for moving in the grid (down, up, right, left)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.grid_size = 0  # Size of the grid
        self.grid = []  # Grid representation
        self.source = None  # Start position
        self.goal = None  # End position
        self.goal_node = None  # Stores the goal node after BFS

    def get_input(self):
        print("\nWelcome to Asma's AI-Based BFS Pathfinding Program!")
        self.grid_size = int(input("\nEnter the grid size (N for N x N): "))

        print("Enter the grid (0 = blocked, 1 = open space):")
        self.grid = [list(map(int, input().split())) for _ in range(self.grid_size)]

        print("Enter source coordinates (row col):", end=" ")
        src_x, src_y = map(int, input().split())

        print("Enter goal coordinates (row col):", end=" ")
        goal_x, goal_y = map(int, input().split())

        # Create source and goal nodes
        self.source = Node(src_x, src_y, 0)
        self.goal = Node(goal_x, goal_y, float('inf'))

    def bfs_search(self):
        queue = deque()
        queue.append(self.source)  # Start BFS from the source

        # Keep track of visited nodes
        visited = [[False] * self.grid_size for _ in range(self.grid_size)]
        visited[self.source.x][self.source.y] = True

        while queue:
            current = queue.popleft()  # Dequeue the current node

            # Check if we reached the goal
            if current.x == self.goal.x and current.y == self.goal.y:
                self.goal_node = current  # Store goal node for path reconstruction
                return True  # Goal found

            # Explore neighboring cells
            for dx, dy in self.directions:
                new_x, new_y = current.x + dx, current.y + dy

                # Check if the move is valid
                if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
                    if self.grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                        visited[new_x][new_y] = True  # Mark as visited
                        queue.append(Node(new_x, new_y, current.level + 1, parent=current))  # Store parent for path

        return False  # Goal not reachable

    def reconstruct_path(self):
        path = []
        current = self.goal_node

        while current:
            path.append((current.x, current.y))  # Store the coordinates
            current = current.parent  # Move to parent node

        return path[::-1]  # Reverse to get path from source to goal

    def run(self):
        self.get_input()  # Take user input

        if self.bfs_search():  # Perform BFS
            print("\nGoal found!")
            print("Number of moves required:", self.goal_node.level)
            print("Path from source to goal:", self.reconstruct_path())
        else:
            print("\nGoal cannot be reached from the starting position.")

if __name__ == "__main__":
    print("Running Asma's AI BFS Pathfinding Program...")
    bfs = BFSPathFinder()
    bfs.run()
