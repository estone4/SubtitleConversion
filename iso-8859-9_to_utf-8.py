from tkinter import *
from tkinter import filedialog


class MyFirstGUI:
    input_file = ""
    file_contents = ""
    decoded_bytes = ""
    output_file = ""

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
        root.filename = filedialog.askopenfilename(initialdir=".", title="Select file", )
        print(root.filename)
        MyFirstGUI.input_file = open(root.filename, "rb")
        MyFirstGUI.file_contents = MyFirstGUI.input_file.read()  # read raw bytes
        try:
            MyFirstGUI.decoded_bytes = str(MyFirstGUI.file_contents.decode("utf-8"))
            print('File decoded as "UTF-8"')
        except Exception as e:
            print('Error decoding file as "UTF-8"')
            print(e)
            print('Decoding file as "ISO-8859-9"')
            MyFirstGUI.decoded_bytes = str(MyFirstGUI.file_contents.decode('ISO-8859-9'))

        if MyFirstGUI.decoded_bytes is not None:
            print(MyFirstGUI.decoded_bytes)

        MyFirstGUI.input_file.close()
        print("Opened " + root.filename)
        print(MyFirstGUI.decoded_bytes)

    def save(self):
        root.filename = filedialog.asksaveasfilename(initialdir=".", title="Save file", )
        MyFirstGUI.output_file = open(root.filename, "w")
        MyFirstGUI.output_file.write(MyFirstGUI.decoded_bytes)
        MyFirstGUI.output_file.close()
        print("Saved file to " + root.filename)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
