import os

#Functions
def Intro_Terminal():
    text = "\nThis is the test file of this project!\n\nOutput of code:"
    print(text)

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


#Constants
#Variables
testmapjes_path = "C:/Users/JoranDelcroix/PycharmProjects/Engineering/File_Manager/Testmapjes"
dir_name = "testmap1"

#Main code
Intro_Terminal()

Make_Dir(testmapjes_path, dir_name)
