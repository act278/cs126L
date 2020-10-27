from letters import *


def main():
    input_string = input("Please enter a message to fancify: ")
    mode = input("Would you like to print the message: "
                 "(V) Vertically or (H) Horizontally?: ")
    if(mode == "V"):
        print_vertical(input_string.upper())
    elif(mode == "H"):
        print_horizontal(input_string.upper())


def letter_to_ascii(letter):
    return letter_bank[letter]


def print_vertical(characters):
    # Prints each character by line
    for char in characters:
        print()
        for line in range(font_line_count):
            print(letter_to_ascii(char)[line])


def print_horizontal(characters):
    # Prints characters by line
    for line in range(font_line_count):
        print()
        for char in characters:
            print(letter_to_ascii(char)[line], end=" ")


if __name__ == "__main__":
    main()
