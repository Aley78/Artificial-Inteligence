from collections import deque

class Solution:
    def __init__(self):
        # Define the goal state and possible moves (up, down, left, right)
        self.goal = '123456780'
        self.moves = {
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
    
    def solve(self, board):
        # Convert the board list to a string representation
        start = ''.join(str(num) for row in board for num in row)
        
        # Check if the initial state is already the goal
        if start == self.goal:
            return 0
        
        # Use a queue for BFS, starting with the initial state and zero moves
        queue = deque([(start, start.index('0'), 0)])  # (current_state, index_of_zero, moves_count)
        visited = set()  # To track visited states
        visited.add(start)
        
        while queue:
            state, zero_pos, moves = queue.popleft()
            
            # Explore all possible moves
            for move in self.moves[zero_pos]:
                # Swap zero position with the new move position
                new_state = list(state)
                new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
                new_state = ''.join(new_state)
                
                # Check if the new state is the goal
                if new_state == self.goal:
                    return moves + 1
                
                # If not visited, add to queue
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, move, moves + 1))
        
        # If no solution found
        return -1

# Example usage:
board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

solver = Solution()
result = solver.solve(board)
print(f"Number of moves to solve: {result}")
