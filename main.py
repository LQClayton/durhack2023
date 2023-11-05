import tkinter as tk
import time

window = tk.Tk()
guiDict = {"myButtonsP":"","myButtonsE":"", "panic":""}

def counting(event):
		for j in range(5):
				for i in range(5):
						print(i+1)
						time.sleep(1)

def rhythm():
		#use with buttons - vibrate if you tap the right ones in a certain amount of time
		pass

def enlarge(event):
		#need some way to take in button information ie text and change the text size
		print(event)
	
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

def make_buttons(myFile,dictKey):
		for i in range(len(myFile)):
				button = tk.Button(text=myFile[i], width=25, height=5, bg="white", fg="pink",)
				button.pack()
				guiDict[dictKey] = button
				button.bind("<Button>", counting)
		button.pack()
		loop()

def make_panic():
		guiDict["panic"] = tk.Button(text="I need to breathe", width=25, height=5, bg="white", fg="pink",)
		guiDict["panic"].pack()
		guiDict["panic"].bind("<Button>", counting)
		loop()

def loop():
		window.mainloop()

def display():
		phraseMake = file_handle("phrases.txt")
		emotionsMake = file_handle("emotions.txt")
		make_buttons(phraseMake, "myButtonsP")
		make_buttons(emotionsMake, "myButtonsE")
		make_panic()
		

display()