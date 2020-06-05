import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import sys
import os
import win32gui, win32con
import pyttsx3 as spk


ForceHideLogger = win32gui.GetForegroundWindow()
win32gui.ShowWindow(ForceHideLogger , win32con.SW_HIDE)


root = Tkinter.Tk(className="imitate notepad")
root.geometry('750x480')
textPad = ScrolledText(root, width=100, height=80)

def open_command():
	file= tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
	if file != None:
		contents = file.read()
		textPad.insert('1.0', contents)
		file.close()
	
def save_command():
	file = tkFileDialog.asksaveasfile(mode='w')
	if file != None:
		data = textPad.get('1.0', END+'-1c')
		file.write(data)
		file.close()

def exit_command():
	if tkMessageBox.askokcancel("Quit", "Do you want to close? "):
		root.destroy()

		
def about_command():
	r = spk.Engine()
	r.say('IMITATE NOTEPAD. writed by: razyar. 2019 by imitate')
	r.runAndWait()
	Label = tkMessageBox.showinfo("About", "IMITATE NOTEPAD \n writed by: razyar \n 2019 by imitate \n https://razyar.ir")
	
def cmd_command():
	os.system('start cmd')
	r = spk.Engine()
	r.say('CMD Runned.')
	r.runAndWait()
	
def dummy():
	filename = sys.argv[0]
	os.system('call %s' % str(filename))
	
	
	
def focus1():
	os.system('call Focus1.mp3')
def focus2():
	os.system('call Believer.mp3')
def focus3():
	os.system('call returntome.mp3')
	
	






#initFile	
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
#finFile

#initHelp
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)
#finhelp


#initopt
optmenu = Menu(menu)
menu.add_cascade(label="Options", menu=optmenu)
optmenu.add_command(label="CMD", command=cmd_command)
#finopt


#initMusic
musicmenu = Menu(menu)
menu.add_cascade(label="Musics", menu=musicmenu)
musicmenu.add_command(label="lsak Danielson - Power", command=focus1)
musicmenu.add_command(label="Imagine Dragons - Believer", command=focus2)
musicmenu.add_command(label="Dean Martin - Return to me", command=focus3)
#finmusic




root.iconbitmap('icon.ico')
W = Label(root, text="IMITATE NOTEPAD", fg="black")
W.pack()
textPad.pack()
root.mainloop()

