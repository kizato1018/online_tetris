import tkinter as tk

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
            command=lambda: controller.show_frame("SingleModePage"))
        button2 = tk.Button(
            self,
            text="多人遊戲",
            command=lambda: controller.show_frame("MultiModePage"))
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


class SingleModePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pageTitleLabel = tk.Label(self, text="SingleMode page")
        pageTitleLabel.pack(side="top", fill="x", pady=10)
        returnButton = tk.Button(
            self,
            text="back",
            command=lambda: controller.show_frame("MainPage"))
        returnButton.pack()


class MultiModePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pageTitleLabel = tk.Label(self, text="MultiMode page")
        pageTitleLabel.pack(side="top", fill="x", pady=10)
        returnButton = tk.Button(
            self,
            text="back",
            command=lambda: controller.show_frame("MainPage"))
        returnButton.pack()


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
