from tkinter import *

window = Tk()

def myClick():
    myLabel = Label(window ,text="Look! I clicked a Button!")
    myLabel.pack()
                    

# Creating a label widget
##myLabel1 = Label(root,text="Hello World!").grid(row=0, column=3)
##myLabel2 = Label(root,text="My name is Lionel Nkabi").grid(row=2, column=3)

#shoving it onto the screen
#myLabel1.grid(row=0, column=3)
#myLabel2.grid(row=1, column=3)

myButton = Button(window, text="Click Me!", padx = 50, command= myClick, fg = "Purple", bg = "Yellow")

myButton.pack()

window.mainloop()
