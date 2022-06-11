#David
import tkinter as tk
#words = re.sub("[^\w]", " ",  mystr).split()
#Converts string to list of words seperated by spaces.
class SpeedyReady:
    def __init__(self, master):
        self.master = master
        frame = tk.Frame(self.master)
        self.text0 = tk.StringVar()
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        myFont = ("Arial", 30)
        label0 = tk.Label(frame, font=myFont, text=self.text0)
        label0.pack(padx = 5, pady = 5)
        label1 = tk.Label(frame, font=myFont, text=self.text1)
        label1.pack(padx = 5, pady = 5)
        label2 = tk.Label(frame, font=myFont, text=self.text2)
        label2.pack(padx = 5, pady = 5)
        frame.pack(padx = 5, pady = 5)

root = tk.Tk()
root.geometry("600x300")
window = SpeedyReady(root)
root.mainloop()