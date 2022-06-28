from tkinter import *

class Window1:

    def __init__(self, master):
        self.master = master
        self.label = Button(self.master, text = "Example", command = self.load_new)
        self.label.pack()

    def load_new(self):
        self.label.destroy()
        ## Code to execute next class

class Window2:

    def __init__(self, master):
        self.master = master
        self.label = Label(self.master, text = "Example")
        self.label.pack()

def main():
    root = Tk()
    run = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()