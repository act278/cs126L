import random


def main():
    board = startup()
    print_screen(board)
    while(lights_on(board)):
        row = int(input("Please choose a row number (0-4): "))
        collumn = int(input("Please choose a collumn number (0-4): "))
        board = toggle_lights(row, collumn, board)
        print_screen(board)
    print("VICTORY!")


def startup():
    board = []
    # Generates a blank array
    for _ in range(5):
        board.append(get_blank_array())
    # Toggles random combinations of lights in the blank array
    for _ in range(50):
        row = random.randint(0, 4)
        collumn = random.randint(0, 4)
        board = toggle_lights(row, collumn, board)
    return board


def get_blank_array():
    blank_array = []
    for _ in range(5):
        blank_array.append(False)
    return blank_array


def print_screen(board):
    for row in range(5):
        for collumn in range(5):
            if(board[row][collumn]):
                print("\N{BLACK SQUARE}", end="  ")
            else:
                print("\N{WHITE SQUARE}", end="  ")
            # When reaching the end of a row, continue onto next line
            if((collumn+1) % 5 == 0):
                print()


def lights_on(board):
    for row in range(5):
        for collumn in range(5):
            if board[row][collumn]:
                return True
    return False


def toggle_right(row, collumn, board):
    board[row][collumn + 1] = switch(board[row][collumn + 1])
    return board


def toggle_left(row, collumn, board):
    board[row][collumn - 1] = switch(board[row][collumn - 1])
    return board


def toggle_up(row, collumn, board):
    board[row - 1][collumn] = switch(board[row - 1][collumn])
    return board


def toggle_down(row, collumn, board):
    board[row + 1][collumn] = switch(board[row + 1][collumn])
    return board


def toggle_lights(row, collumn, board):
    board[row][collumn] = switch(board[row][collumn])
    # Checks for edge cases (literally)
    if(row == 0):
        board = toggle_down(row, collumn, board)
        if(collumn == 4):
            board = toggle_left(row, collumn, board)
        elif(collumn == 0):
            board = toggle_right(row, collumn, board)
        else:
            board = toggle_right(row, collumn, board)
            board = toggle_left(row, collumn, board)
    elif(row == 4):
        board = toggle_up(row, collumn, board)
        if(collumn == 4):
            board = toggle_left(row, collumn, board)
        elif(collumn == 0):
            board = toggle_right(row, collumn, board)
        else:
            board = toggle_right(row, collumn, board)
            board = toggle_left(row, collumn, board)
    elif(collumn == 0):
        board = toggle_down(row, collumn, board)
        board = toggle_up(row, collumn, board)
        board = toggle_right(row, collumn, board)
    elif(collumn == 4):
        board = toggle_down(row, collumn, board)
        board = toggle_up(row, collumn, board)
        board = toggle_left(row, collumn, board)
    # For lights in the middle
    else:
        board = toggle_down(row, collumn, board)
        board = toggle_up(row, collumn, board)
        board = toggle_right(row, collumn, board)
        board = toggle_left(row, collumn, board)
    return board


def switch(value):
    if(value):
        return False
    else:
        return True


main()
