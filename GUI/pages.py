import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

image_path = os.path.dirname(os.path.abspath(__file__)) + '/image'

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
            command=lambda: controller.start_game("SingleMode"))
        button2 = tk.Button(
            self,
            text="多人遊戲",
            command=lambda: controller.start_game("MultiMode"))
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
        tableWidth = 10
        tableHeight = 20
        
        # page title
        pageTitleLabel = tk.Label(self, text="SingleMode page")

        # table
        self.table = tk.Frame(self, pady=100)

        for i in range(tableWidth):
            for j in range(tableHeight):
                img = ImageTk.PhotoImage(
                    image=Image.open('{}/defaultblock.png'.format(image_path)).resize(
                        size=(20, 20)))
                imageLabel = tk.Label(self.table, image=img)
                imageLabel.image = img
                imageLabel.grid(column=x, row=y)

        # Layout for whole page
        pageTitleLabel.grid(column=0, row=0)
        self.table.grid(column=0, row=1)


class MultiModePage(tk.Frame):
    def __init__(self, parent, controller):
        # Initialization
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tableWidth = 10
        tableHeight = 20

        # page title
        pageTitleLabel = tk.Label(self, text="MultiMode page")

        # table
        self.table = tk.Frame(self, pady=100)

        for x in range(tableWidth):
            for y in range(tableHeight):
                img = ImageTk.PhotoImage(
                    image=Image.open('{}/defaultblock.png'.format(image_path)).resize(
                        size=(20, 20)))
                imageLabel = tk.Label(self.table, image=img)
                imageLabel.image = img
                imageLabel.grid(column=x, row=y)

        # Layout for whole page
        pageTitleLabel.grid(column=0, row=0)
        self.table.grid(column=0, row=1)
