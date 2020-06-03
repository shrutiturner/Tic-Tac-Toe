def tic_tac_toe():
    # 9 spaces to fill the dictionary of moves with blanks to show the beginning of the game
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
                    if endgame is not None:
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


def check_winner(board):
    # Create a matrix of the values for further testing
    matrix = [[board[(1, 3)], board[(2, 3)], board[(3, 3)]],
              [board[(1, 2)], board[(2, 2)], board[(3, 2)]],
              [board[(1, 1)], board[(2, 1)], board[(3, 1)]]]

    # Is there a winner in a row?
    for row in matrix:
        if row[0] == row[1] == row[2] != " ":
            winner = row[0]
            return "{0} wins".format(winner)

    # Is there a winner in a column?
    i = 0
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != " ":
            winner = matrix[0][i]
            return "{0} wins".format(winner)
        i += 1

    # Is there a winner in a diagonal, but not multiple?
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        winner = matrix[0][0]
        return "{0} wins".format(winner)

    if matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":
        winner = matrix[0][2]
        return "{0} wins".format(winner)

    # decide on output statement based on maximum number of turns remaining
    blank_count = sum(x.count(' ') for x in matrix)

    if blank_count == 0:
        return "Draw"
    else:
        return None


def print_board(board):
    """print board layout from moves_dict"""
    print("---------")
    print("| {0} {1} {2} |".format(board[(1, 3)], board[(2, 3)], board[(3, 3)]))
    print("| {0} {1} {2} |".format(board[(1, 2)], board[(2, 2)], board[(3, 2)]))
    print("| {0} {1} {2} |".format(board[(1, 1)], board[(2, 1)], board[(3, 1)]))
    print("---------")


tic_tac_toe()



