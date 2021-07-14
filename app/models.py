import os
import numpy as np
from copy import deepcopy
from objects import *

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Model():
    def __init__(self):
        # the seven type of block
        brick_types = [Brick("I"),Brick("J"),Brick("L"),Brick("O"),Brick("S"),Brick("T"),Brick("Z")]
        self.brick = np.random.choice(brick_types)
        self.position = Position(3,1)
    def table_height(self):
        self.height = 20
        return self.height
    def table_width(self):
        self.width = 10
        return self.width

    def my_table_init(self):
        self.table = Table(self.height, self.width)
        # setup the wall
        for i in range(self.height + 10):
            for j in range(self.width + 10):
                if (i == 0 or j == 0 or i == self.height or j == self.width + 1):
                    self.table.bufferedTable[i][j] = Block("red")
                else:
                    self.table.bufferedTable[i][j] = Block()
    
    def screen_clear(self):
        # for mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows platfrom
            _ = os.system('cls')
    
    def rotate(self):
        npbrick = np.array(self.brick)
        # rotate right 90 degree
        rotate_matrix = np.rot90(npbrick, 3)
        return rotate_matrix
    
    # actions
    def action_left(self):
        self.position.x -= 1
    def action_right(self):
        self.position.x += 1
    def action_up(self):
        # rotate
        self.brick = self.rotate(self.brick)
    def action_down(self):
        # speed up
        pass

    # check whether the block collision in table
    def collision(self, table, block, position) -> bool:
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
    
    # fall down one step and return the whole table
    def falldown(self, block: np.array, table,pos):
        cur_table = deepcopy(table)
        if (not self.collision(table, block, pos)):
            pos.y += 1
            cur_table = self.combineTableAndBlock(table, block, pos)
        return deepcopy(cur_table)