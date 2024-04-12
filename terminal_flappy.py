import os
import time
import keyboard

#global
matrix: list[str] = [
    "---------------------------------------------------------",
    "         |                     |                    |    ",
    "         |                     |                    |    ",
    "         |                     |                         ",
    "         |                     |                         ",
    "                               |                         ",
    "                               |                    |    ",
    "                               |                    |    ",
    "         |                                          |    ",
    "         |                                          |    ",
    "         |                                          |    ",
    "         |                     |                    |    ",
    "----------------------------------------------------------"
]

position: int = 4
##

def shift_columns_left(matrix) -> list:
    new_matrix: list = []
    for row in matrix:

        new_row = row[1:] + row[0]
        new_matrix.append(new_row)
    return new_matrix

def check_collision(pos: int, matrix: list) -> bool:
    return matrix[pos][1] == '|'

def scene(pos: int) -> str:
    global matrix
    # Always shift columns to the left
    matrix = shift_columns_left(matrix)
    for i in range(len(matrix)):
        if i != pos:
            matrix[i] = matrix[i].replace('>', ' ')

    if ' ' in matrix[pos]:
        matrix[pos] = matrix[pos].replace(' ', '>', 1)

    return "\n".join(matrix)

def game_loop():
    global position  # Add this line to refer to the global position variable
    while True:
        print(scene(position))
        time.sleep(0.3)
        os.system('cls')  # It's generally better to clear the screen after printing to avoid flickering

        space_pressed = keyboard.is_pressed("space")
        if position < len(matrix) - 1 and not space_pressed and not check_collision(position + 1, matrix):
            position += 1
        elif space_pressed and position > 1 and not check_collision(position - 1, matrix):
            position -= 1
        elif check_collision(position, matrix):
            print("You hit a PIPE!")
            time.sleep(3)
            break
        else:
            print("You lost")
            time.sleep(3)
            break
        



if __name__ == '__main__':
    game_loop()
