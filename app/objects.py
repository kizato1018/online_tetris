import numpy as np


class Block():
    def __init__(self, color: str = "black"):
        self.color = color
        if color == "black":
            self.value = 0
        else:
            self.value = 1


class Table():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.bufferedTable = [[Block("grey") for i in range(width + 10)]
                              for j in range(height + 10)]

    def get_real_table(self):
        table = [[Block("grey") for i in range(self.width)]
                 for j in range(self.height)]
        for h in range(self.height):
            for w in range(self.width):
                table[h][w] = self.bufferedTable[h][w]
        return table


class Brick:
    def __init__(self, type):
        self.type = type
        self.value = [[Block() for i in range(4)] for j in range(4)]
        color = "#" + "".join(
            map(hex, list(np.random.choice(range(256), size=3))))
        if (type == "I"):
            self.value[0][1] = Block(color)
            self.value[1][1] = Block(color)
            self.value[2][1] = Block(color)
            self.value[3][1] = Block(color)
        if (type == "J"):
            self.value[0][1] = Block(color)
            self.value[1][1] = Block(color)
            self.value[1][2] = Block(color)
            self.value[1][3] = Block(color)
        if (type == "L"):
            self.value[0][3] = Block(color)
            self.value[1][1] = Block(color)
            self.value[1][2] = Block(color)
            self.value[1][3] = Block(color)
        if (type == "O"):
            self.value[0][1] = Block(color)
            self.value[0][2] = Block(color)
            self.value[1][1] = Block(color)
            self.value[1][2] = Block(color)
        if (type == "S"):
            self.value[0][2] = Block(color)
            self.value[0][3] = Block(color)
            self.value[1][1] = Block(color)
            self.value[1][2] = Block(color)
        if (type == "T"):
            self.value[0][2] = Block(color)
            self.value[1][1] = Block(color)
            self.value[1][2] = Block(color)
            self.value[1][3] = Block(color)
        if (type == "Z"):
            self.value[0][1] = Block(color)
            self.value[0][2] = Block(color)
            self.value[2][2] = Block(color)
            self.value[2][3] = Block(color)
