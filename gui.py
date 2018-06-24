from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class MyFirstGUI:

    file_contents = ""

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.open_button = Button(master, text="Open File", command=self.open)
        self.open_button.pack()

        self.save_button = Button(master, text="Save File", command=self.save)
        self.save_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def open(self):
        #root.filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("srt files", "*.srt"),("all files","*.*")))
        root.filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",)
        print(root.filename)
        input_file = open(root.filename, "r", encoding="ISO-8859-9")
        MyFirstGUI.file_contents = input_file.read()
        print(MyFirstGUI.file_contents)
        input_file.close()
        print("Opened " + root.filename)

    def save(self):
        print(MyFirstGUI.file_contents)
        root.filename = filedialog.asksaveasfilename(initialdir = ".",title = "Save file",)
        output_file = open(root.filename, "w", encoding="utf-8")
        output_file.write(MyFirstGUI.file_contents)
        output_file.close()

#file_contents = ""
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()