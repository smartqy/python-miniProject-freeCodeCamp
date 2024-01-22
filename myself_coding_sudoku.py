from pprint import pprint

def find_next_empty(puzzle):

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j
    
    return None,None

def valid_guess(puzzle, guess, row, col):

    if guess in puzzle[row]:
        return False
    
    # for i in range(9):
    #     if guess == puzzle[i][col]:
    #         return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
        
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if guess == puzzle[i][j]:
                return False
            
    return True


def solve_sudoku(puzzle):
    
    row, col = find_next_empty(puzzle)

    if row == None:
        return True
    
    for guess in range(1,10):
        if valid_guess(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
        example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
        print(solve_sudoku(example_board))
        pprint(example_board)
      
    
