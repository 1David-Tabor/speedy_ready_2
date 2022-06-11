#David
import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
#words = re.sub("[^\w]", " ",  mystr).split()
#Converts string to list of words seperated by spaces.
class SpeedyReady:
    def __init__(self, master):
        self.master = master
        frame = ttk.Frame(self.master)
        self.text0 = tk.StringVar()
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        style = ttk.Style()
        style.configure("Custom.TLabel",foreground="white",
                                        background="red",
                                        padding=[10, 10, 10, 10],
                                        font=("Helvetica", 25),
                                        relief = "raised")
        label0 = ttk.Label(frame, text=self.text0, style="Custom.TLabel")
        label0.pack(padx = 5, pady = 5)
        label1 = ttk.Label(frame, text=self.text1, style="Custom.TLabel")
        label1.pack(padx = 5, pady = 5)
        label2 = ttk.Label(frame, text=self.text2, style="Custom.TLabel")
        label2.pack(padx = 5, pady = 5)
        frame.pack(padx = 5, pady = 5)

root = tk.Tk()
root.geometry("600x300")
window = SpeedyReady(root)
root.mainloop()