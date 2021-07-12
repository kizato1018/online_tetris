from PIL import ImageTk, Image
import logging
import tkinter as tk
import sys

from blocks import Block


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
        self.grid_rowconfigure(0, weight=1)
        tableWidth = 10
        tableHeight = 20

        # page title
        pageTitleLabel = tk.Label(self, text="SingleMode page")

        # table
        self.table = tk.Frame(self, pady=100)

        for x in range(tableWidth):
            for y in range(tableHeight):
                block = Block("default")
                imageLabel = tk.Label(self.table, image=block.image)
                imageLabel.image = block.image
                imageLabel.grid(column=x, row=y)

        # Layout for whole page
        pageTitleLabel.grid(column=0, row=0)
        self.table.grid(column=0, row=1)

    def change_block_type(self, x: int, y: int, block: Block):
        imageLabel = tk.Label(self.table, image=block.image)
        imageLabel.image = block.image
        imageLabel.grid(column=x, row=y)


class MultiModePage(tk.Frame):
    def __init__(self, parent, controller):
        pass
