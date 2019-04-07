from tkinter import *
from tkinter import filedialog


class MyFirstGUI:

    file_contents = ""

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.open_button = Button(master, text="Open File", command=self.open_file)
        self.open_button.pack()

        self.save_button = Button(master, text="Save File", command=self.save_file)
        self.save_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def open_file(self):
        # TODO: check if the file has already been converted before continuing"
        # root.filename = tkFileDialog.askopenfilename(initial_dir = ".",title = "Select file",file_types = \
        # (("srt files", "*.srt"),("all files","*.*")))
        root.filename = filedialog.askopenfilename(initial_dir = ".",title="Select file",)
        print(root.filename)
        input_file = open(root.filename, "r", encoding="ISO-8859-9")
        MyFirstGUI.file_contents = input_file.read()
        print(MyFirstGUI.file_contents)
        input_file.close()
        print("Opened " + root.filename)

    def save_file(self):
        print(MyFirstGUI.file_contents)
        root.filename = filedialog.asksaveasfilename(initial_dir = ".",title="Save file",)
        output_file = open(root.filename, "w", encoding="utf-8")
        output_file.write(MyFirstGUI.file_contents)
        output_file.close()
        print("Saved file to " + root.filename)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
