"""Lesson 7 assignment"""
"""Use the Tkinter module and your creativity to draw a picture
composed of at least five shapes. Use the animation techniques 
described in the lesson to move at least one of the shapes on 
your Canvas."""

from tkinter import *
from time import *

class myFrame(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.myCanvas = Canvas(width="800", height="500", bg="lightblue")
		self.myCanvas.grid()

		
		"""Create rainbow"""
		self.myCanvas.create_arc(644, 155, 155, 675, start=0, extent=180, width="25", outline="red")
		self.myCanvas.create_arc(622, 178, 178, 650, start=0, extent=180, width="25", outline="orange")
		self.myCanvas.create_arc(600, 200, 200, 625, start=0, extent=180, width="25", outline="yellow")
		self.myCanvas.create_arc(578, 221, 221, 625, start=0, extent=180, width="25", outline="green")
		self.myCanvas.create_arc(555, 242, 242, 625, start=0, extent=180, width="25", outline="blue")
		self.myCanvas.create_arc(532, 264, 264, 625, start=0, extent=180, width="25", outline="purple")
		"""This is the grass bottom"""
		self.myCanvas.create_rectangle(0, 400, 800, 500, fill="green")
		"""This is the brown house base"""
		self.myCanvas.create_rectangle(450, 300, 600, 400, fill="brown")
		self.myCanvas.create_line(450, 310, 600, 310)
		self.myCanvas.create_line(450, 320, 600, 320)
		self.myCanvas.create_line(450, 330, 600, 330)
		self.myCanvas.create_line(450, 340, 600, 340)
		self.myCanvas.create_line(450, 350, 600, 350)
		self.myCanvas.create_line(450, 360, 600, 360)
		self.myCanvas.create_line(450, 370, 600, 370)
		self.myCanvas.create_line(450, 380, 600, 380)
		self.myCanvas.create_line(450, 390, 600, 390)
		"""This is the roof of the house"""
		self.myCanvas.create_polygon((450, 300, 525, 250, 600, 300), fill="darkblue")
		"""This is the windows of the house"""
		self.myCanvas.create_rectangle(470, 320, 500, 350, fill="white")
		self.myCanvas.create_rectangle(550, 320, 580, 350, fill="white")
		"""This is the door of the house"""
		self.myCanvas.create_rectangle(510, 340, 540, 400, fill="blue")

		my_sun = self.myCanvas.create_oval(10, 10, 50, 50, fill="yellow", outline="yellow")

		for c in range(76):
			i = 10*c
			self.myCanvas.coords(my_sun, 10+i, 20, 50+i, 60)
			self.myCanvas.update()
			sleep(0.1)

frame01 = myFrame()
frame01.mainloop()