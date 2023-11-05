import tkinter as tk
import time

def counting():
    #while page is running
    for i in range(5):
        print(i+1)
        time.sleep(1)

def rhythm():
    #use with buttons
    pass

def file_handle(filename):
    with open(filename, 'r') as f:
        x = f.readlines()
    f.close()
    x = clean_list(x)
    return x

def clean_list(myList):
    for i in range(len(myList)):
        myList[i] = myList[i].replace("\n","")
    return myList

def brain_no_function():
    myFile1 = file_handle("emotions.txt")
    myFile2 = file_handle("phrases.txt")
    print(myFile1, myFile2)

def make_buttons(myFile):
    newList = []
    for i in range(len(myFile)):
        button = tk.Button(text=myFile[i],width=25, height=5, bg="white", fg="pink",)
        button.pack()
        newList.append(button)

def display():
    window = tk.Tk()
    phraseMake = file_handle("phrases.txt")
    make_buttons(phraseMake)


display()