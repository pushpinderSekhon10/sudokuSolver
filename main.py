def is_valid_move(board, row, col, number):
    # Check the row
    for x in range(9):
        if board[row][x] == number:
            return False

    # Check the column
    for x in range(9):
        if board[x][col] == number:
            return False

    # Check the 3x3 box
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if board[corner_row + x][corner_col + y] == number:
                return False
    return True

def solve(board, row, col):
    if col == 9:  # If the column is 9, we're outside the board, move to next row
        if row == 8:  # If the row is also the last one, we've solved the puzzle
            return True
        return solve(board, row + 1, 0)  # Start next row, reset col to 0

    if board[row][col] > 0:  # Skip already filled cells
        return solve(board, row, col + 1)

    for num in range(1, 10):  # Try all numbers from 1 to 9
        if is_valid_move(board, row, col, num):
            board[row][col] = num  # Place the number
            if solve(board, row, col + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False  # Trigger backtracking if no number fits

board = [
    [0, 5, 1, 3, 4, 9, 0, 0, 0],
    [9, 2, 0, 0, 0, 0, 4, 5, 0],
    [0, 0, 3, 2, 0, 6, 9, 1, 0],
    [6, 0, 0, 1, 3, 0, 0, 0, 0],
    [7, 3, 0, 5, 0, 0, 6, 2, 0],
    [2, 0, 9, 7, 0, 4, 0, 8, 0],
    [5, 0, 8, 0, 2, 0, 0, 3, 0],
    [3, 4, 2, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 6, 0, 3, 0, 4, 0]
]

if solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
else:
    print("No solution")
