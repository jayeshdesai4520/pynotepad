import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    root = Tk()

    # default window width and height
    Width = 300
    Height = 300
    TextArea = Text(root)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    EditMenu = Menu(MenuBar, tearoff=0)
    HelpMenu = Menu(MenuBar, tearoff=0)

    # To add scrollbar
    ScrollBar = Scrollbar(TextArea)
    file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.Width = kwargs['width']
        except KeyError:
            pass

        try:
            self.Height = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.root.title("Untitled - Notepad")

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.Width / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.Height / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' % (self.Width,
                                              self.Height,
                                              left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.TextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.Menu.add_command(label="New",
                                        command=self.File)

        # To open a already existing file
        self.FileMenu.add_command(label="Open",
                                        command=self.openFile)

        # To save current file
        self.FileMenu.add_command(label="Save",
                                        command=self.saveFile)

        # To create a line in the dialog
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit",
                                        command=self.quitApplication)
        self.MenuBar.add_cascade(label="File",
                                       menu=self.thisFileMenu)

        # To give a feature of cut
        self.EditMenu.add_command(label="Cut",
                                        command=self.cut)

        # to give a feature of copy
        self.EditMenu.add_command(label="Copy",
                                        command=self.copy)

        # To give a feature of paste
        self.EditMenu.add_command(label="Paste",
                                        command=self.paste)

        # To give a feature of editing
        self.MenuBar.add_cascade(label="Edit",
                                       menu=self.EditMenu)

        # To create a feature of description of the notepad
        self.HelpMenu.add_command(label="About Notepad",
                                        command=self.showAbout)
        self.MenuBar.add_cascade(label="Help",
                                       menu=self.HelpMenu)

        self.root.config(menu=self.MenuBar)

        self.ScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.ScrollBar.set)

    def quitApplication(self):
        self.root.destroy()
        # exit()

    def showAbout(self):
        showinfo("Notepad", "made by jayesh desai :)")

    def openFile(self):

        self.file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # Try to open the file
            # set the window title
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.TextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.TextArea.insert(1.0, file.read())

            file.close()

    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0, END)

    def saveFile(self):

        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:

                # Try to save the file
                file = open(self.file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.root.title(os.path.basename(self.file) + " - Notepad")


        else:
            file = open(self.file, "w")
            file.write(self.TextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.TextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.root.mainloop()

    # Run main application


notepad = Notepad(width=600, height=400)
notepad.run()