"""Practice with Tkinter"""
from tkinter import *

class MyFrame(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.myCanvas = Canvas(width=300, height=200, bg="teal")
		self.myCanvas.grid()
		self.myCanvas.create_rectangle(50, 50, 250, 150, outline="white", width="1", fill="black")
		self.myCanvas.create_oval(53, 53, 247, 147, outline="yellow", width="1", fill="green")
		self.myCanvas.create_line(1, 1, 48, 48, arrow="last")
		self.myCanvas.create_line(300, 200, 252, 152, arrow="last")
		self.myCanvas.create_line(300, 1, 252, 48, arrow="last")
		self.myCanvas.create_line(1, 200, 48, 152, arrow="last")
		self.myCanvas.create_text(150, 100, text="Hello World!", fill="black", anchor="s", font=("Calibri", 16))
		self.myCanvas.create_text(150, 100, text="Secondary text object", fill="black", anchor="n", font=("Calibri", 14))

frame02 = MyFrame()
frame02.mainloop()
