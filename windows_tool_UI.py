import os
from tkinter import *
from PIL import Image
from scipy import misc
from tkinter import filedialog


def resize(image_location : str,save_location : str, length : int, breadth : int):
    for i in os.listdir(image_location):
        image = Image.open(image_location + "\\{}".format(i))
        image = image.resize((length,breadth))
        image.save(save_location + "\\resized_{}".format(i))



def convert(string):
    string = string.split("\\")
    print(string)  

def rename(directory,name,start):
    files = os.listdir(directory)
    for i in files:
        os.rename(directory + "\\" + i, directory + "\\" + name + str(start))
        start += 1



main = Tk(screenName="Windows Tool")

main.geometry("250x225")

main.title("Window Tool")

Label(main,text = "Directory").grid(row = 0,column = 0)
Label(main,text = "Name").grid(row = 1,column = 0)
Label(main,text = "Start").grid(row = 2,column = 0)




directory = Entry(main)
directory.grid(row = 0,column = 1)
name = Entry(main)
name.grid(row = 1,column = 1)
start = Entry(main)
start.grid(row = 2,column = 1)

def getdetails():
    rename(directory.get(),name.get(),int(start.get()))
    print("Done")



renaming = Button(main,text = "Rename",command = getdetails).grid(row = 4,column = 0)
Label(main,text = "").grid(row = 5,column = 0)

Label(main,text = "Directory").grid(row = 6,column = 0)
Label(main,text = "Save Directory").grid(row = 7,column = 0)
Label(main,text = "Length").grid(row = 8,column = 0)
Label(main,text = "Breadth").grid(row = 9,column = 0)

image_directory = Entry(main)
image_directory.grid(row = 6,column = 1)
save_directory = Entry(main)
save_directory.grid(row = 7,column = 1)
length = Entry(main)
length.grid(row = 8,column = 1)
breadth = Entry(main)
breadth.grid(row = 9,column = 1)

def resizing():
    resize(image_directory.get(),save_directory.get(),int(length.get()),int(breadth.get()))


resize_button = Button(main,text = "Resize",command = resizing).grid(row = 10,column = 0)

Label(main,text = "").grid(row = 11,column = 0)


exit_button = Button(main,text = "Exit",command = main.destroy,bg = "Red").grid(row = 10,column= 1 )

main.mainloop()