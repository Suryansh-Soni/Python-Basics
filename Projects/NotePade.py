# "tkinter" for gui(graphical user interface) app 
#  module(single python file) and libarary (bunch of module)
# filedialog:allows users to select files or folders for opening/saving, returning paths
# messagebox :displays alert, info, or error messages to the user
import tkinter as tk
from tkinter import filedialog,messagebox

# main window code
root=tk.Tk()
root.title("My Notpad")
root.geometry("800x600")
# create test area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Arial",12)
)
text.pack(expand=True,fill=tk.BOTH)

# main logc :
# function to create a new file:
def newFile():
    text.delete(1.0,tk.END)
# function 2: open a new file
def openFile():
    # open file dialogue
    filePath=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if filePath:
        with open(filePath,"r") as f:
            text.delete(1.0,tk.END)
            text.insert(tk.END ,f.read())
# function 3:Save the file
def saveFile():
    filePath=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if filePath:
        with open(filePath,"w") as f:
            f.write(text.get(1.0,tk.END))
    
    messagebox.showinfo("Info","File run successfully")

# Menu Bar
menu=tk.Menu(root)
root.config(menu=menu)
fileMenu=tk.Menu(menu)
# new open,save,exit
menu.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=root.quit)



# start and keep window open 
root.mainloop()


