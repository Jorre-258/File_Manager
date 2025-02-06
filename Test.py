import os
from tkinter import *
import tkinter

#Functions
def Intro_Terminal():
    TerminalText = "\nThis is the test file of this project!\n\nOutput of code:"
    print(TerminalText)
    TkText = Text(root, height=4, width=40)
    TkText.pack()
    TkText.insert(END, "Welcome to this file sorter.")


def Make_Dir(path, name):
    try: 
        os.chdir(path)
    except FileNotFoundError:
        print("Did not find this directory")
    except:
        print("There has been an error")

    try:
        str(name)
        os.mkdir(name)
        print("Succesfully made this directory:", name)
    except FileExistsError:
        print("This folder already exists")
    except:
        print("There has been an error")


#Constants
#Variables
testmapjes_path = "C:/Users/JoranDelcroix/PycharmProjects/Engineering/File_Manager/Testmapjes"
dir_name = "Test"
root = tkinter.Tk()

root.geometry("1000x800")
#Main code
Intro_Terminal()

#Make_Dir(testmapjes_path, dir_name)

root.title("Test")
TestText = Label(root,text="TestTest")
TestText.pack()

root.mainloop()

#Source https://www.geeksforgeeks.org/python-gui-tkinter/