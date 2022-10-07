import pyautogui
from tkinter import *
from tkinter.filedialog import *

root = Tk()

root.geometry('180x30')

def takescreenshot():
	ms = pyautogui.screenshot()
	sp = asksaveasfilename()
	ms.save(sp+".png")

myButton = Button(text ="Screen Shot", command = takescreenshot , font = 5).pack(side='top')

root.mainloop()
