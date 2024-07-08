import curses
import shutil
import random
from time import sleep


def game_loop(window):
    #setup inicial
    curses.curs_set(0)
    snake = generate_random_snake_position()
    
    while True:
        draw_screen(window=window)
        draw_actor(ator=snake, window=window)

        direction = get_new_direction(window=window, timeout=1000) 
        if direction is not None:
            move_actor(actor=snake, direction=direction)
        if actor_hit_border(actor=snake, window, window):
            return
        


def draw_screen(window):
    window.clear
    window.border(0)

def draw_actor(actor, window):
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)

def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
        return direction
    return None

def move_actor(actor, direction):
     match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_RIGHT:
            actor[1] += 1

def actor_hit_border(actor, window):
    heigh, width = window.getmaxyx()

    if (actor[0] <= 0) or (actor[0] >= heigh-1):
        return    
    if (actor[1] <= 0) or (actor[1] >= width-1):
        return 
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)

        
        
       

       


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
    print("Perdeu!")