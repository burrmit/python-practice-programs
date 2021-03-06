from tkinter import *

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("200x200")
       self.master.title("My GUI")
       self.grid()

       self.button_click_here = Button(self, text = "Click Me", command = self.click_here_click)
       self.button_click_here.grid()

       self.my_text = StringVar()
       self.message = Label(self, textvariable = self.my_text)
       self.my_text.set("Come on press the button!")
       self.message.grid()

   def click_here_click(self):
   	   self.my_text.set("You did it!")

frame01 = MyFrame()
frame01.mainloop()