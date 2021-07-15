from tkinter import font
from tkinter.constants import CENTER
from PIL import ImageTk, Image
import logging
import tkinter as tk
import sys

from objects import Block, Table


class View():
    def __init__(self, master, controller) -> None:
        self.controller = controller
        self.master = master
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.frame = MainPage(parent=self.master, controller=self.controller)
        self.frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name) -> bool:
        for frame in self.master.winfo_children():
            frame.destroy()
        self.frame = getattr(sys.modules[__name__],
                             page_name)(parent=self.master,
                                        controller=self.controller)
        self.frame.grid(row=0, column=0, sticky="nsew")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pageTitleLabel = tk.Label(self, text="Main page")
        pageTitleLabel['font'] = "helvetica 30"
        pageTitleLabel.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(
            self,
            text="單人遊戲",
            command=lambda: controller.initialize_game("SingleMode"))
        button2 = tk.Button(
            self,
            text="多人遊戲",
            command=lambda: controller.initialize_game("MultiMode"))
        button3 = tk.Button(
            self,
            text="設定",
            command=lambda: controller.show_frame("SettingPage"))
        button4 = tk.Button(
            self,
            text="規則",
            command=lambda: controller.show_frame("RulesPage"),
        )
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pageTitleLabel = tk.Label(self, text="Setting page")
        pageTitleLabel.pack(side="top", fill="x", pady=10)
        returnButton = tk.Button(
            self,
            text="back",
            command=lambda: controller.show_frame("MainPage"))
        returnButton.pack()


class RulesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pageTitleLabel = tk.Label(self, text="Rules page")
        pageTitleLabel.pack(side="top", fill="x", pady=10)
        returnButton = tk.Button(
            self,
            text="back",
            command=lambda: controller.show_frame("MainPage"))
        returnButton.pack()


class SingleModePage(tk.Frame):
    def __init__(self, parent, controller):
        # Initialization
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.blockLength = 20
        self.padding = 0
        self.score = 100

        # page title
        pageTitleLabel = tk.Label(self, text="SingleMode page")

        # score
        scoreLabel = tk.Label(self,
                              text=str(self.score),
                              textvariable=str(self.score),
                              justify=CENTER,
                              font=('Times', 24, 'bold italic underline'),
                              bg="red")

        # Layout for whole page
        pageTitleLabel.grid(column=0, row=0)
        scoreLabel.grid(column=1, row=0)

    def initialize_gametable(self, tableWidth, tableHeight):
        # table
        self.tableCanva = tk.Canvas(
            self,
            width=(tableWidth + 2) * (self.blockLength + self.padding),
            height=(tableHeight + 2) * (self.blockLength + self.padding))
        self.tableCanva.grid(column=0, row=1)
        for x in range(tableWidth + 2):
            for y in range(tableHeight + 2):

                x_0 = x * (self.blockLength + self.padding) + self.padding
                y_0 = y * (self.blockLength + self.padding) + self.padding
                x_1 = x * (self.blockLength +
                           self.padding) + self.blockLength + self.padding
                y_1 = y * (self.blockLength +
                           self.padding) + self.blockLength + self.padding
                if x == 0 or x == tableWidth + 1 or y == 0 or y == tableHeight + 1:
                    self.tableCanva.create_rectangle(x_0,
                                                     y_0,
                                                     x_1,
                                                     y_1,
                                                     fill="grey",
                                                     outline="black")
                else:
                    self.tableCanva.create_rectangle(x_0,
                                                     y_0,
                                                     x_1,
                                                     y_1,
                                                     fill=Block().color,
                                                     outline="black")

    def update_table_canva(self, table: Table):
        for x in range(table.width + 2):
            for y in range(table.height + 2):

                x_0 = x * (self.blockLength + self.padding) + self.padding
                y_0 = y * (self.blockLength + self.padding) + self.padding
                x_1 = x * (self.blockLength +
                           self.padding) + self.blockLength + self.padding
                y_1 = y * (self.blockLength +
                           self.padding) + self.blockLength + self.padding
                if x == 0 or x == table.width + 1 or y == 0 or y == table.height + 1:
                    self.tableCanva.create_rectangle(x_0,
                                                     y_0,
                                                     x_1,
                                                     y_1,
                                                     fill="grey",
                                                     outline="black")
                else:
                    self.tableCanva.create_rectangle(
                        x_0,
                        y_0,
                        x_1,
                        y_1,
                        fill=table.get_real_table()[x][y].color,
                    )

    def update_score(self, score):
        self.score = score


class MultiModePage(tk.Frame):
    def __init__(self, parent, controller):
        pass
