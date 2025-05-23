from collections import deque


class Node:
    def __init__(self, x, y, level):
        self.x = x  # x-coordinate of the node
        self.y = y  # y-coordinate of the node
        self.level = level  # level of the node in the BFS tree


class BFS:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible movement directions (down, up, right, left)
        self.found = False  # Flag to indicate whether goal is found
        self.goal_level = 0  # Level of the goal node
        self.N = 0  # Size of the grid
        self.source = None  # Source node
        self.goal = None  # Goal node

    def init(self):
        # Take user input for the grid
        self.N = int(input("Enter the size of the grid (N x N): "))
        graph = []
        print("Enter the grid (0 for blocked, 1 for open space):")
        for i in range(self.N):
            row = list(map(int, input().split()))
            graph.append(row)

        # Take user input for the source and goal positions
        source_x, source_y = map(int, input("Enter the source coordinates (x y): ").split())
        goal_x, goal_y = map(int, input("Enter the goal coordinates (x y): ").split())

        # Create Node objects for source and goal
        self.source = Node(source_x, source_y, 0)  # Start from source with level 0
        self.goal = Node(goal_x, goal_y, float('inf'))  # Goal node with initially infinite level

        # Perform BFS
        self.st_bfs(graph)

        # Print result
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
        else:
            print("Goal cannot be reached from starting block")

    def st_bfs(self, graph):
        queue = deque()
        queue.append(self.source)  # Enqueue the source node

        # Breadth-first search
        while queue:
            u = queue.popleft()  # Dequeue the front node

            # Explore neighbors
            for dx, dy in self.directions:
                v_x, v_y = u.x + dx, u.y + dy  # Calculate neighbor's coordinates

                # Check if neighbor is within grid boundaries and is a valid move
                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                    v_level = u.level + 1  # Increment level (distance)

                    if v_x == self.goal.x and v_y == self.goal.y:  # Check if neighbor is the goal
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        return

                    graph[v_x][v_y] = 0  # Mark neighbor as visited (set to 0)

                    # Create a new node for the neighbor and enqueue it
                    child = Node(v_x, v_y, v_level)
                    queue.append(child)


if __name__ == "__main__":
    bfs = BFS()  # Create BFS instance
    bfs.init()  # Initialize and run BFS5
