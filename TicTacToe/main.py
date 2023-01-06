

def has_won(play_board):
    first_elements = []
    for row in play_board:
        if row[0] == row[1] and row[1] == row[2]:
            print(f"{row[0]} sign wins")
        print(f"Appending element: {row[0]}")
        first_elements.append(row[0])
        print(first_elements)
    if first_elements[0] == first_elements[1] and first_elements[1] == first_elements[2]:
        print(f"{first_elements[0]} sign has won")


def play_tic_tac_toe():
    row_1 = [None] * 3
    row_2 = [None] * 3
    row_3 = [None] * 3
    play_board = [row_1, row_2, row_3]
    moves_remaining = 3
    acceptable_values = [1, 2, 3]
    column = 1
    row = 1
    while(moves_remaining > 0 and column in acceptable_values and row in acceptable_values):
        user_input = input("Enter 'x' or 'o' signs \n").lower()
        if (user_input == "x" or user_input == "o"):
            print("Enter column, then row numbers respectively to position your input sign")
            column = int(input("Column number: "))
            print(f"column number = {column}")
            row = int(input("Row number: "))
            print(f"row number = {row}")
            play_board[row - 1][column - 1] = user_input
            moves_remaining -= 1
        else:
            print("Not a valid input")
            break
    has_won(play_board)
    print(play_board)

play_tic_tac_toe()