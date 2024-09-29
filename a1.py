from collections import deque

class EightPuzzleSolver:
    def __init__(self):
        # Define the goal state and possible moves for each tile position
        self.goal_state = '123456780'
        self.move_options = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }
    
    def solve_puzzle(self, board):
        # Convert the 2D board list into a single string for easy comparison
        start_state = ''.join(str(num) for row in board for num in row)
        
        # Check if the starting state is already the goal state
        if start_state == self.goal_state:
            return 0
        
        # Initialize the BFS queue with the initial state, position of the blank (zero), and move count
        queue = deque([(start_state, start_state.index('0'), 0)])  # (current_state, zero_index, step_count)
        visited = set()  # To track visited states to avoid revisits
        visited.add(start_state)
        
        while queue:
            current_state, blank_index, step_count = queue.popleft()
            
            # Explore all possible moves from the current blank (zero) position
            for next_index in self.move_options[blank_index]:
                # Swap the blank tile with the adjacent tile to create a new state
                new_state = list(current_state)
                new_state[blank_index], new_state[next_index] = new_state[next_index], new_state[blank_index]
                new_state_str = ''.join(new_state)
                
                # Check if the new state is the goal state
                if new_state_str == self.goal_state:
                    return step_count + 1
                
                # If the new state hasn't been visited, add it to the queue
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, next_index, step_count + 1))
        
        # If no solution is found, return -1
        return -1

# Example usage:
board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

solver = EightPuzzleSolver()
result = solver.solve_puzzle(board)
print(f"Number of moves to solve the puzzle: {result}")
