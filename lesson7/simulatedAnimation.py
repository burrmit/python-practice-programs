"""Working with simulated program animation, but pausing time"""

from tkinter import *
from time import *

class myFrame(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.myCanvas = Canvas(width="810", height="100", bg="black")
		self.myCanvas.grid()

		my_rect_id = self.myCanvas.create_rectangle(20, 20, 60, 60, fill="yellow")

		for c in range(76):
			i = 10*c
			self.myCanvas.coords(my_rect_id, 20+i, 20, 60+i, 60)
			self.myCanvas.update()
			sleep(0.1)

frame01 = myFrame()
frame01.mainloop()