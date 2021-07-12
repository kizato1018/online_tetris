from tkinter.constants import TRUE
import tkinter as tk
import logging
import time

from models import Model
from views import View
from blocks import Block


class Controller():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Online tetris")
        self.root.resizable(TRUE, TRUE)
        self.root.minsize(width=500, height=300)
        self.root.mainloop()

    def show_frame(self, page_name):
        logging.debug(f"Show Frame {page_name}")
        self.view.show_frame(page_name)

    def initialize_game(self, gamemode: str):
        logging.info("Game initializing...")
        self.show_frame(f'{gamemode}Page')
        self.root.update()
        self.start_game(gamemode)

    def start_game(self, gamemode: str):
        logging.info("Game start")
        self.autoAddBlock()

    def blockUpdate(self, x: int, y: int, blocktype: str):
        block = Block(blocktype)
        self.view.frame.change_block_type(x=x, y=y, block=block)
        self.root.update()
        logging.info(f"Update block {x},{y} to {block.type}")

    def autoAddBlock(self):
        logging.info("start auto AddBlock")
        for y in range(10):
            self.blockUpdate(0, y, "red")
            time.sleep(1)
