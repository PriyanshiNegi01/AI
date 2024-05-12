# Sudoku puzzle
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_sudoku(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(puzzle[i][j], end=" ")
        print()

print_sudoku(puzzle)

def find_empty_location(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def is_valid(puzzle, num, row, col):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(puzzle):
    empty_loc = find_empty_location(puzzle)
    if not empty_loc:
        return True
    row, col = empty_loc
    for num in range(1, 10):
        if is_valid(puzzle, num, row, col):
            puzzle[row][col] = num
            if solve_sudoku(puzzle):
                return True
            puzzle[row][col] = 0
    return False

# Driver code

if solve_sudoku(puzzle):
    print("*" * 7 + "Solution" + "*" * 7)
    print_sudoku(puzzle)

else:
    print("No solution exists.")
