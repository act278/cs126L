from letters import *

def main():
    print(letter_bank["A"])
    letter_to_ascii("A")
    input_string = input("Please enter a message to fancify: ")
    mode = input("Would you like to print the message: (V) Vertically or (H) Horizontally?: ")
    if(mode == "V"):
        print_vertical(str(input_string.upper()))
    elif(mode == "H"):
        print_horizontal(input_string.upper())


def letter_to_ascii(letter):
    return letter_bank[letter]


def print_vertical(characters):
    for char in characters:
        print()
        for line in range(font_line_count):
            print(letter_to_ascii(char)[line])


def print_horizontal(characters):
    for line in range (font_line_count):
        print()
        for char in characters:
            print(letter_to_ascii(char)[line], end=" ")


if __name__ == "__main__":
    main()
