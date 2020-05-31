def move_legality(input_str):
    # Have a legal number of moves been made by each side?

    x_count = input_str.count('X')
    o_count = input_str.count('O')
    blank_count = input_str.count('_')

    # Create a matrix of the values for further testing

    matrix = [[input_str[0], input_str[1], input_str[2]],
              [input_str[3], input_str[4], input_str[5]],
              [input_str[6], input_str[7], input_str[8]]]

    # Is there a winner in a row, but not multiple?
    row_win_count = 0

    for row in matrix:
        if row[0] == row[1] == row[2] != "_":
            row_win_count += 1
            winner = row[0]

    # Is there a winner in a column, but not multiple?
    column_win_count = 0
    i = 0

    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != "_":
            column_win_count += 1
            winner = matrix[0][i]
        i += 1

    # Is there a winner in a diagonal, but not multiple?
    diagonal_win_count = 0

    if matrix[0][0] == matrix[1][1] == matrix[2][2] != "_":
        diagonal_win_count += 1
        winner = matrix[0][0]

    if matrix[0][2] == matrix[1][1] == matrix[2][0] != "_":
        diagonal_win_count += 1
        winner = matrix[0][2]

    # decide on output statement based on values calculated

    if row_win_count + column_win_count + diagonal_win_count > 1:
        return "Impossible"
    elif x_count > o_count + 1 or o_count > x_count + 1:
        return "Impossible"
    elif row_win_count + column_win_count + diagonal_win_count == 1:
        return "{0} wins".format(winner)
    elif blank_count > 0:
        return "Game not finished"
    else:
        return "Draw"

