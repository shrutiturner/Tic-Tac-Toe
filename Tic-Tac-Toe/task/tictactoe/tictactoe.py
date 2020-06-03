def check_winner(moves_dict):
    # Convert moves_dict into an input string
    input_str = f'{moves_dict[(1, 3)]}{moves_dict[(2, 3)]}{moves_dict[(3, 3)]}' \
                f'{moves_dict[(1, 2)]}{moves_dict[(2, 2)]}{moves_dict[(3, 2)]}' \
                f'{moves_dict[(1, 1)]}{moves_dict[(2, 1)]}{moves_dict[(3, 1)]}'

    # count turns
    blank_count = input_str.count(' ')

    # Create a matrix of the values for further testing
    matrix = [[input_str[0], input_str[1], input_str[2]],
              [input_str[3], input_str[4], input_str[5]],
              [input_str[6], input_str[7], input_str[8]]]

    # Is there a winner in a row, but not multiple?
    row_win_count = 0

    for row in matrix:
        if row[0] == row[1] == row[2] != " ":
            row_win_count += 1
            winner = row[0]

    # Is there a winner in a column, but not multiple?
    column_win_count = 0
    i = 0

    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != " ":
            column_win_count += 1
            winner = matrix[0][i]
        i += 1

    # Is there a winner in a diagonal, but not multiple?
    diagonal_win_count = 0

    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        diagonal_win_count += 1
        winner = matrix[0][0]

    if matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":
        diagonal_win_count += 1
        winner = matrix[0][2]

    # decide on output statement based on values calculated

    if row_win_count + column_win_count + diagonal_win_count == 1:
        return "{0} wins".format(winner)
    elif blank_count == 0:
        return "Draw"
    else:
        return None


def print_board(moves_dict):
    """print board layout from moves_dict"""
    print("---------")
    print("| {0} {1} {2} |".format(moves_dict[(1, 3)], moves_dict[(2, 3)], moves_dict[(3, 3)]))
    print("| {0} {1} {2} |".format(moves_dict[(1, 2)], moves_dict[(2, 2)], moves_dict[(3, 2)]))
    print("| {0} {1} {2} |".format(moves_dict[(1, 1)], moves_dict[(2, 1)], moves_dict[(3, 1)]))
    print("---------")


# input_str = input("Enter the coordinates:")

input_str = '         '

moves_dict = {(1, 3): input_str[0], (2, 3): input_str[1], (3, 3): input_str[2],
              (1, 2): input_str[3], (2, 2): input_str[4], (3, 2): input_str[5],
              (1, 1): input_str[6], (2, 1): input_str[7], (3, 1): input_str[8]}

print_board(moves_dict)

turn = 0


while True:
    if turn % 2 == 0:
        go = 'X'
    else:
        go = 'O'

    move_str = input("Enter the coordinates:").replace(" ", "")
    if len(move_str) == 2:
        coords = (int(move_str[0]), int(move_str[1]))
        if coords in moves_dict.keys():
            if moves_dict[coords] == ' ':
                moves_dict[coords] = go
                print_board(moves_dict)
                turn += 1
                endgame = check_winner(moves_dict)
                if endgame != None:
                    print_board(moves_dict)
                    print(endgame)
                    break
                else:
                    continue
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")






