from tkinter import *
from tkinter import filedialog

def openfile():
    myInitialDir = "C:/Users/Lionel/Documents/FreecodeCamp/GUI with Python and TKinter"
    myTitle= "Open File and Attenadance text file"
    myFileTypes = ("text files","*.txt"),("All files","*.*")

    filepath = filedialog.askopenfilename(
        title = myTitle,
        initialdir = myInitialDir,
        filetypes=(myFileTypes)
    )
    print(filepath)

    
root = Tk()

#root.title('Time and Attendance System')
button = Button(text="Open", command=openfile)
button.pack()

root.mainloop()
