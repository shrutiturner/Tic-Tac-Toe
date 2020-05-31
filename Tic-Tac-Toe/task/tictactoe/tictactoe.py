def print_board(moves_dict):
    """print board layout from moves_dict"""
    print("---------")
    print("| {0} {1} {2} |".format(moves_dict[(1, 3)], moves_dict[(2, 3)], moves_dict[(3, 3)]))
    print("| {0} {1} {2} |".format(moves_dict[(1, 2)], moves_dict[(2, 2)], moves_dict[(3, 2)]))
    print("| {0} {1} {2} |".format(moves_dict[(1, 1)], moves_dict[(2, 1)], moves_dict[(3, 1)]))
    print("---------")


input_str = input("Enter cells:")

moves_dict = {(1, 3): input_str[0], (2, 3): input_str[1], (3, 3): input_str[2],
              (1, 2): input_str[3], (2, 2): input_str[4], (3, 2): input_str[5],
              (1, 1): input_str[6], (2, 1): input_str[7], (3, 1): input_str[8]}

print_board(moves_dict)

while True:
    move_str = input("Enter the coordinates:").replace(" ", "")
    if len(move_str) == 2:
        coords = (int(move_str[0]), int(move_str[1]))
        if coords in moves_dict.keys():
            if moves_dict[coords] == '_':
                print(moves_dict)
                moves_dict[coords] = "X"
                print(moves_dict)
                break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

print_board(moves_dict)



