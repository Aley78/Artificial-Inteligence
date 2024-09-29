import heapq

class State:
    def __init__(self, value, parent, start, goal):
        self.value = value  # Current state value (e.g., grid position)
        self.parent = parent  # Parent state
        self.start = start  # Initial state
        self.goal = goal  # Goal state
        self.dist = self.GetDistance()  # Heuristic (distance to goal)

    def GetDistance(self):
        """
        Heuristic function to estimate distance to goal.
        For a grid, we can use the Manhattan distance.
        """
        # Assuming value is a tuple (x, y) for grid coordinates
        x1, y1 = self.value
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance

    def CreateChildren(self):
        """
        Generate possible child states (moves) from current state.
        Assuming we can move in 4 directions (up, down, left, right).
        """
        children = []
        x, y = self.value
        # Possible moves (up, down, left, right)
        moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        
        for move in moves:
            if self.IsValid(move):  # Ensure the move is valid (inside grid)
                child = State(move, self, self.start, self.goal)
                children.append(child)
        return children

    def IsValid(self, pos):
        """
        Check if the new position is within valid boundaries (grid bounds).
        Assuming a grid size of 5x5 for simplicity.
        """
        x, y = pos
        if 0 <= x < 5 and 0 <= y < 5:  # Assuming grid boundaries are 5x5
            return True
        return False

    # Add the less-than method for priority comparison
    def __lt__(self, other):
        """
        Override the less-than operator to compare states based on their distance.
        This is necessary for using the state in a priority queue.
        """
        return self.dist < other.dist

class A_Star_Solver:
    def __init__(self, start, goal):
        self.path = []  # To store the final path
        self.visitedQueue = set()  # To track visited nodes
        self.priorityQueue = []  # To store nodes to be visited (heap queue)
        self.start = start  # Start state
        self.goal = goal  # Goal state

    def Solve(self):
        start_state = State(self.start, None, self.start, self.goal)
        heapq.heappush(self.priorityQueue, (start_state.dist, start_state))
        
        while self.priorityQueue:
            # Get the state with the lowest heuristic distance
            current_state = heapq.heappop(self.priorityQueue)[1]
            
            # If we reached the goal, reconstruct the path
            if current_state.value == self.goal:
                return self.ReconstructPath(current_state)

            # Mark current state as visited
            self.visitedQueue.add(current_state.value)

            # Expand children
            children = current_state.CreateChildren()
            for child in children:
                if child.value not in self.visitedQueue:
                    heapq.heappush(self.priorityQueue, (child.dist, child))
                    self.visitedQueue.add(child.value)

        # If no solution is found
        return None

    def ReconstructPath(self, state):
        """
        Reconstruct the path from goal to start by following the parent pointers.
        """
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return path[::-1]  # Reverse the path to get from start to goal

# Example usage:
if __name__ == "__main__":
    # Start at (0, 0) in a grid and goal is (4, 4)
    start = (0, 0)
    goal = (4, 4)

    solver = A_Star_Solver(start, goal)
    solution = solver.Solve()

    if solution:
        print(f"Path to solution: {solution}")
    else:
        print("No solution found.")
