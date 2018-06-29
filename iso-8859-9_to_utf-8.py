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

        self.label = Label(master, text="ISO-8859-9 to UTF-8")
        self.label.pack()

        self.open_button = Button(master, text="Open File", command=self.open)
        self.open_button.pack()

        self.save_button = Button(master, text="Save File", command=self.save)
        self.save_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    # TODO: try reading the bytes to be able to perform bitwise operations to check for utf-8 s

    def open(self):
        self.master.filename = filedialog.askopenfilename(initialdir=".", title="Select file", )
        print(self.master.filename)
        with open(self.master.filename, "rb") as f:
            self.file_contents = f.read()  # read raw bytes
        try:
            self.decoded_bytes = str(self.file_contents.decode("utf-8"))
            print('File decoded as "UTF-8"')
        except Exception as e:
            print('Error decoding file as "UTF-8"')
            print(e)
            print('Decoding file as "ISO-8859-9"')
            self.decoded_bytes = str(self.file_contents.decode('ISO-8859-9'))

        if self.decoded_bytes is not None:
            print(self.decoded_bytes)

        f.close()
        print("Opened " + self.master.filename)
        print(self.decoded_bytes)

    def save(self):
        self.master.filename = filedialog.asksaveasfilename(initialdir=".", title="Save file", )
        with open(self.master.filename, "w") as f:
            f.write(self.decoded_bytes)
        f.close()
        print("Saved file to " + self.master.filename)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
