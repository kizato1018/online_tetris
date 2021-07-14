from tkinter.constants import TRUE
import tkinter as tk
import logging
import time
from pynput import keyboard

from models import Model
from views import View
from objects import Block



class Controller():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Online tetris")
        self.root.resizable(TRUE, TRUE)
        self.root.minsize(width=500, height=300)
        self.root.mainloop()

    

    def initialize_game(self, gamemode: str):
        tableWidth = 10
        tableHeight = 20
        logging.info("Game initializing...")
        self.show_frame(f'{gamemode}Page')
        self.view.initialize_gametable(tableWidth, tableHeight)
        self.root.update()
        self.init_keyboard_controls()
        self.start_game(gamemode)

    def init_keyboard_controls(self):
        self.controls = {
            'Key.left':  self.model.action_left,
            'Key.right': self.model.action_right,
            'Key.up': self.model.action_up,
            'Key.down': self.model.action_down,
        }
        self.key_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.key_listener.start()

    def show_frame(self, page_name):
        logging.debug(f"Show Frame {page_name}")
        self.view.show_frame(page_name)

    def update_table_canva(self):
        table = self.model.table
        self.view.update_table_canva(table)

    def start_game(self, gamemode: str):
        logging.info("Game start")

    def single_mode_game():
        pass
    
    def multi_mode_game():
        pass

    