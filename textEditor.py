# Axel Bau  Neks
from tkinter import *
from tkinter import filedialog as fileDialog
from io import open
# var

routeFile = ""

# fuctions


def new():
    global routeFile  # the var's changes will be global
    message.set("New file")
    routeFile = ""
    text.delete(1.0, 'end')  # parameter settings /start - end/


def openFile():
    global routeFile
    message.set("Open file")
    routeFile = fileDialog.askopenfilename(initialdir='.', filetypes=(
        ("File text", "*.txt"),),
        title="Open a file text ")
    if routeFile != "":
        file = open(routeFile, 'r')
        contents = file.read()
        text.delete(1.0, 'end')
        text.insert('insert', contents)
        file.close()


def save():
    message.set("Save")
    if routeFile != "":
        contents = text.get(1.0, 'end-1c')
        file = open(routeFile, 'w+')
        file.write(contents)
        message.set("Saved file")
    else:
        saveAs()


def saveAs():
    global routeFile
    message.set("Save as")
    file = fileDialog.asksaveasfilename(
        title="Save the file as", mode="w", defaultextension=".txt")
    if file is not None:
        routeFile = file.name
        contents = text.get(1.0,'end-1c')
        file = open(routeFile,'w+')
        file.write(contents)
        file.close()
        message.set("The file was saved correctly")
    else:
        message.set("Save canceled")
        routeFile = ""


# root settings
root = Tk()
root.title("Text Editor")
root.iconbitmap("iconTexteditor.ico")
# Menu bar
menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=new)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=save)
fileMenu.add_command(label="Saves as", command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)


menuBar.add_cascade(label="File", menu=fileMenu)


# text's box
text = Text(root)

text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("consoles"))
# Make a bottom display

message = StringVar()
message.set("Welcome at the text's editor")
display = Label(root, textvar=message, justify='left')
display.pack(side="left")
# initialize from root
root.mainloop()
