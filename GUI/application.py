import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import TRUE
from GUI.pages import *


class OnlineTetrisMenu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Online tetris")
        self.resizable(TRUE, TRUE)
        self.minsize(width=500, height=300)

        # Container for pages(frames)
        container = ttk.Frame(self, padding="3 3 12 12")
        container.pack(side="top", fill="both", expand=True)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # pages
        self.frames = {}
        for F in (MainPage, SettingPage, RulesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def start_game(self, gamemode: str):
        self.newWindow = Game(gamemode=gamemode)
        self.withdraw()


class Game(tk.Tk):
    def __init__(self, gamemode, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.gamemode = gamemode
        self.title("Online tetris")
        self.resizable(TRUE, TRUE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #self.minsize(width=500, height=300)

        # Container for pages(frames)
        container = ttk.Frame(self, padding="8 8 12 12")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        container.grid(column=0, row=0)

        # pages
        self.frames = {}
        for F in (SingleModePage, MultiModePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("{}Page".format(gamemode))

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
