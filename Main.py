import os
import tkinter
from tkinter import *

#Functions
def Intro():
    print("The is a file sorter made by Joran Delcroix \n\nOutput of the code:")
    TkText = Label(root, text="Welcome to this file sorter made by Joran Delcroix", font=("Arial", 30))
    TkText.pack()

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
        print("This file already exists")
    except:
        print("There has been an error")


#Variables
root = tkinter.Tk()
root.geometry("1000x600")
root.title("")

#Start of the code
os.system("cls || clear")
Intro()

listbox = Listbox(root)

path = input("Please enter the path of the folder you want to sort.")

#path = r"C:\Users\JoranDelcroix\PycharmProjects\Engineering\File_Manager\Testmapjes"
path = path.replace('\\', '/')
files = []
try:
    files = os.listdir(path)
except FileNotFoundError:
    print("This path does not exist")
except:
    print("There has been an error")

dir_name = "Test"
if files != []:
    print("This are the files that are in this folder:")
    tkinter.Label(root, text="These are the files of your chosen folder.").pack()
    for file in files:
        print(file)
        listbox.insert(END, file)

scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Attach the Scrollbar to the Listbox
listbox.config(yscrollcommand=scrollbar.set)
root.mainloop()
#Make_Dir(path, dir_name)
