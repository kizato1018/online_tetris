import random
import os
import numpy as np
import keyboard
from time import sleep
from copy import deepcopy


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# build up the wall
def table_init(T,h,w,b):
    for i in range(h + b):
        for j in range(w + b):
            if (i == 0 or j == 0 or i == h or j == w + 1):
                T[i][j] = 1
            else:
                T[i][j] = 0


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def rotate(block):
    npblock = np.array(block)
    # rotate right 90 degree
    rotate_matrix = np.rot90(npblock, 3)
    return rotate_matrix

def show(table,h,w):
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if (table[i][j] == 0):
                print("| _ ", end="")
            else:
                print("| O ", end="")
        print("|")


# falldown feature
def falldown(block: np.array, table,pos,h,w,sp):
    cur_table = deepcopy(table)
    ActionMove(pos,block)
    while (not collision(table, block, pos)):
        screen_clear()
        show(cur_table,h,w)
        sleep(sp)
        print("")
        cur_table = combineTableAndBlock(table, block, pos)
        pos.y += 1
    screen_clear()
    show(cur_table,h,w)
    sleep(0.5)
    print("")
    return deepcopy(cur_table)


# check whether the block collision in table
def collision(table, block, position) -> bool:
    for i in range(4):
        for j in range(4):
            if (table[position.y + i][position.x + j] == 1
                    and block[i][j] == 1):
                return True


# put the block into the tmp_table and return tmp_table
def combineTableAndBlock(base_table: list(), block, position):
    tmp_table = deepcopy(base_table)
    for i in range(4):
        for j in range(4):
            tmp_table[position.y +
                      i][position.x +
                         j] = block[i][j] or tmp_table[position.y +
                                                       i][position.x + j]
    return deepcopy(tmp_table)

# actions
def ActionLeft(pos):
    pos.x -= 1
def ActionRight(pos):
    pos.x += 1
def ActionUp(block):
    block = rotate(block)


# user_action for direction
def ActionMove(pos,block):
    keyboard.on_press_key("left",lambda _:ActionLeft(pos))
    keyboard.on_press_key("right",lambda _:ActionRight(pos))


def GameStatus(table,w):
    for i in range(1,w+1):
        if(table[1][i] == 1):
            return False
    return True

if __name__ == "__main__":
    # Initialize
    height = 20
    width = 10
    bias = 10
    position = Position(3, 1)
    game_status = True
    block_types = [
        [
            [0, 1, 0, 0],  #type "I"
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ],
        [
            [0, 1, 0, 0],  #type "J"
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 0, 1],  #type "L"
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],  #type "O"
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 1],  #type "S"
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0],  #type "T"
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],  #type "Z"
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
    ]  # the seven type of block
    speed = 0.5

    main_table = [[0 for i in range(width + bias)]
                  for j in range(height + bias)
                  ]  # the screen platform no block:0/have block:1 status
    table_init(main_table,height,width,bias)

    while(game_status):
        # fall down position
        position.y = 1
        position.x = 3
        # get random block feom block_types
        cur_block = np.array(random.choice(block_types))
        main_table = falldown(cur_block, main_table,position,height,width,speed)
        game_status = GameStatus(main_table,width)
    
