def print_chessboard(board):
    """Displays the chessboard with queens in a readable format."""
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    # Check the same row to the left
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check the upper diagonal on the left
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    # Check the lower diagonal on the left
    for r, c in zip(range(row, n), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True

def place_queens(board, col, n):
    """Attempts to place queens on the chessboard using backtracking."""
    # Base case: All queens are placed
    if col >= n:
        return True

    # Try placing a queen in all rows of the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            # Place a queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            if place_queens(board, col + 1, n):
                return True

            # Backtrack if placing the queen leads to no solution
            board[row][col] = 0

    # Return False if the queen cannot be placed in any row of this column
    return False

def solve_n_queens(n):
    """Solves the N-Queens problem for a given board size."""
    # Initialize an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Attempt to solve the N-Queens problem and print the solution
    if not place_queens(board, 0, n):
        print("No solution exists for the given size.")
        return False

    print_chessboard(board)
    return True

# Input: Ask the user for the size of the board
n = int(input("Enter the number of queens: "))
solve_n_queens(n)
