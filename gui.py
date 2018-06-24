from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.open_button = Button(master, text="Open File", command=self.open)
        self.open_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def open(self):
        root.filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("srt files", "*.srt"),("all files","*.*")))
        print(root.filename)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
