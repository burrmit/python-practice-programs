"""Getting a tuple back from a function"""
from tkinter import *

class myFrame(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.myCanvas = Canvas(width="500", height="500")
		self.myCanvas.grid()

		self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
		self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
		self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

		print("Find all shapes")
		print(self.myCanvas.find_enclosed(0, 0, 30, 70))

		print("Find first shape")
		print(self.myCanvas.find_enclosed(0, 0, 30, 30))

		print("Find second shape")
		print(self.myCanvas.find_enclosed(0, 20, 30, 50))

		print("Find third shape")
		print(self.myCanvas.find_enclosed(0, 40, 30, 70))

		print("Find no shape")
		print(self.myCanvas.find_enclosed(0, 0, 1, 1))

frame01 = myFrame()
frame01.mainloop()
