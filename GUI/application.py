import tkinter as tk
from tkinter import ttk
from tkinter.constants import TRUE
from GUI.pages import *

class OnlineTetrisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Online tetris")
        self.resizable(TRUE, TRUE)
        self.minsize(width=500, height=300)

        # Container for pages(frames)
        container = ttk.Frame(self, padding="3 3 12 12")
        container.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # pages
        self.frames = {}
        for F in (MainPage, SingleModePage, MultiModePage, SettingPage,
                  RulesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainPage")

    def show_frame(self, page_name): 
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()