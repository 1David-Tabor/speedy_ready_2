#David
import tkinter as tk
import tkinter.ttk as ttk

class SpeedyReady:
    def __init__(self, master):
        self.master = master
        frame = ttk.Frame(self.master)
        style = ttk.Style()
        style.configure("Custom.TLabel",foreground="white",
                                        background="red",
                                        padding=[10, 10, 10, 10],
                                        relief = "raised")
        label = ttk.Label(frame, text = "Hello World", style = "Custom.TLabel")
        label.pack(padx = 5, pady = 5)
        frame.pack(padx = 5, pady = 5)

root = tk.Tk()
root.geometry("200x150")
window = SpeedyReady(root)
root.mainloop()