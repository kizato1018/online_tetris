from tkinter.constants import TRUE
import tkinter as tk
import logging
import time
from pynput import keyboard
import threading

from models import Model
from views import View
from objects import Block

import logconfig


class Controller():
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Online tetris")
        self.root.resizable(TRUE, TRUE)
        self.root.minsize(width=500, height=300)
        self.init_keyboard_controls()
        self.keydown = False
        self.root.mainloop()

    def initialize_game(self, gamemode: str):
        tableWidth = 10
        tableHeight = 20
        logging.info("Game initializing...")
        # init game GUI
        self.show_frame(f'{gamemode}Page')

        # init gametable
        self.view.frame.initialize_gametable(tableWidth, tableHeight)

        # init game control key
        self.controls['key.left'] = self.model.action_left
        self.controls['key.right'] = self.model.action_right
        #self.controls['key.up'] = self.model.action_up
        self.controls['key.down'] = self.model.action_down

        self.root.update()

        self.start_game(gamemode)

    def on_press(self, keyname):
        """handler for keyboard listener"""
        if self.keydown:
            return
        try:
            self.keydown = True
            keyname = str(keyname).strip('\'')
            logging.debug('+' + keyname)
            if keyname == 'Key.esc':
                pass
            if keyname in self.controls:
                key_handler = self.controls[keyname]
                key_handler()
        except AttributeError:
            logging.error('special key {0} pressed'.format(keyname))

    def on_release(self, keyname):
        """Reset on key up from keyboard listener"""
        self.keydown = False
        keyname = str(keyname).strip('\'')
        logging.debug('-' + keyname)
        if keyname in self.controls:
            key_handler = self.controls[keyname]
            key_handler()

    def init_keyboard_controls(self):
        self.controls = dict()
        self.key_listener = keyboard.Listener(on_press=self.on_press,
                                              on_release=self.on_release)
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
