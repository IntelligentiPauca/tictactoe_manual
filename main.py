"""
TicTacToe game - Put X and O in line to win.

A project to practise Python skills. All moves require manual input of coordinates.

Based on Simple TicTacToe project from JetBrains Academy / HyperSkill
https://hyperskill.org/projects/73

"""


turn_symbol = 'O'
turns_to_draw = 9
state_game = ""
grid = " " * 9
grid_matrix = [[grid[0], grid[1], grid[2]], [grid[3], grid[4], grid[5]], [grid[6], grid[7], grid[8]]]


def print_board():
    print('---------')
    print('|', grid_matrix[0][0], grid_matrix[0][1], grid_matrix[0][2], '|')
    print('|', grid_matrix[1][0], grid_matrix[1][1], grid_matrix[1][2], '|')
    print('|', grid_matrix[2][0], grid_matrix[2][1], grid_matrix[2][2], '|')
    print('---------')


print_board()

while True:
    x, y = input("Enter the coordinates: ").split()
    if x.isdigit() and y.isdigit():
        x = int(x) - 1
        y = int(y) - 1
        if not ((0 <= x <= 2) and (0 <= y <= 2)):
            print("Coordinates should be from 1 to 3!")
        else:
            if grid_matrix[x][y] == ' ':
                if turn_symbol == 'O':
                    turn_symbol = 'X'
                else:
                    turn_symbol = 'O'
                turns_to_draw -= 1

                grid_matrix[x][y] = turn_symbol
                print_board()
                # Analysis
                winning_combos = [(grid_matrix[0][0] + grid_matrix[0][1] + grid_matrix[0][2]),
                                  (grid_matrix[1][0] + grid_matrix[1][1] + grid_matrix[1][2]),
                                  (grid_matrix[2][0] + grid_matrix[2][1] + grid_matrix[2][2]),
                                  (grid_matrix[0][0] + grid_matrix[1][0] + grid_matrix[2][0]),
                                  (grid_matrix[0][1] + grid_matrix[1][1] + grid_matrix[2][1]),
                                  (grid_matrix[0][2] + grid_matrix[1][2] + grid_matrix[2][2]),
                                  (grid_matrix[0][0] + grid_matrix[1][1] + grid_matrix[2][2]),
                                  (grid_matrix[2][0] + grid_matrix[1][1] + grid_matrix[0][2])]

                for line in winning_combos:
                    if line == 'XXX':
                        state_game = "X wins"
                    elif line == 'OOO':
                        state_game = "O wins"

                if turns_to_draw == 0 and not state_game.endswith("wins"):
                    state_game = "Draw"

                if state_game.endswith("wins") or state_game == "Draw":
                    print(state_game)
                    break

                continue
            else:
                print('This cell is occupied! Choose another one!')
    else:
        print('You should enter numbers!')
