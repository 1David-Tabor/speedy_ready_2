#David
import tkinter as tk
from tkinter import ttk, Frame
#words = re.sub("[^\w]", " ",  mystr).split()
#Converts string to list of words seperated by spaces.
class SpeedyReady(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.tabs = ttk.Notebook(self)
        self.tabs.pack()
        self.inputFrame = Frame(self.tabs)
        self.readingFrame = Frame(self.tabs)
        self.readingTabSetup()
        self.inputTabSetup()

        #readingframe.pack(padx = 5, pady = 5)
    def readingTabSetup(self):
        self.tabs.add(self.inputFrame, text='Input')
        self.tabs.add(self.readingFrame, text='Read')
        self.text0 = tk.StringVar()
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        myFont = ("Courier",44)
        label0 = tk.Label(self.readingFrame, font=myFont, text=self.text0)
        label0.pack(padx = 5, pady = 5)
        label1 = tk.Label(self.readingFrame, font=myFont, text=self.text1)
        label1.pack(padx = 5, pady = 5)
        label2 = tk.Label(self.readingFrame, font=myFont, text=self.text2)
        label2.pack(padx = 5, pady = 5)

    def inputTabSetup(self):
        entryField = tk.Text(self.inputFrame, height=8)
        entryField.pack()
        

window = SpeedyReady()
window.mainloop()