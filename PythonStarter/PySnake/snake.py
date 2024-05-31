import curses
import shutil
import random
from time import sleep


def game_loop(window):
    
    snake = generate_random_snake_position()
    window.addch(snake[0], snake[1], curses.ACS_DIAMOND)
    while True:
        window.timeout(1000)
        char = window.getch()
        window.clear()
        match char:
            case curses.KEY_UP:
                snake[0] -= 1
            case curses.KEY_LEFT:
                snake[1] -= 1
            case curses.KEY_DOWN:
                snake[0] += 1
            case curses.KEY_RIGHT:
                snake[1] += 1
            case _: #não apertou tecla ou apertou outra tecla
                pass    
        window.addch(snake[0], snake[1], curses.ACS_DIAMOND)


def get_terminal_size():
    size = shutil.get_terminal_size()
    return size.lines, size.columns

def generate_random_snake_position():
    rows, columns = get_terminal_size()
    snake_y = random.randint(0, rows - 1)
    snake_x = random.randint(0, columns - 1)
    return [snake_y, snake_x]

if __name__ == "__main__":
    curses.wrapper(game_loop)