from tkinter import *

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("500x400")
       self.master.title("Your Personal Information")
       self.grid()

       self.prompt1 = Label(self, text = "First Name:")
       self.prompt1.grid(row = 0, column = 0)

       self.firstname = Entry(self)
       self.firstname.grid(row = 0, column = 1)

       self.prompt2 = Label(self, text = "Last Name:")
       self.prompt2.grid(row = 1, column = 0)

       self.lastname = Entry(self)
       self.lastname.grid(row = 1, column = 1)

       self.prompt3 = Label(self, text = "Date of birth:")
       self.prompt3.grid(row = 2, column = 0)

       self.dob = Entry(self)
       self.dob.grid(row = 2, column = 1)

       self.button_submit = Button( self, text = "Submit",
           command = self.submit_click )
       self.button_submit.grid(columnspan = 2, pady = 10)

       self.my_text = StringVar()
       self.message = Label(self, textvariable = self.my_text)
       self.message.grid(columnspan = 2)

       self.sample_label = Label(self, text="Some Sample Text", font = "Courier 10")
       self.sample_label.grid(row = 5, column = 0, columnspan = 2)

       self.bold_on = IntVar()
       self.check_bold = Checkbutton(self, text = "Bold",
          variable = self.bold_on, command = self.set_font)
       self.check_bold.grid(row = 6, column = 0)

       self.underline_on = IntVar()
       self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
       self.check_underline.grid(row = 6, column = 1)

       self.point_size = StringVar()
       self.point_size.set("10")
       self.ten_point = Radiobutton(self, text = "10 point",
               variable = self.point_size, value = "10",
               command = self.set_font)
       self.ten_point.grid(row = 7, column = 0)

       self.twelve_point = Radiobutton(self, text = "12 point",
               variable = self.point_size, value = "12",
               command = self.set_font)
       self.twelve_point.grid(row = 7, column = 1)

       self.family = StringVar()
       self.times = Radiobutton(self, text = "Times",
               variable = self.family, value = "times",
               command = self.set_font)
       self.times.grid(row = 8, column = 0)

       self.helvetica = Radiobutton(self, text = "Helvetica",
               variable = self.family, value = "helvetica",
               command = self.set_font)
       self.helvetica.grid(row = 8, column = 1)

   def submit_click(self):
       output_message = "Hello " + self.firstname.get() + ", our records indicate your last name is: " + self.lastname.get() + ", and your date of birth is: " + self.dob.get()
       self.my_text.set(output_message)

   def set_font(self):
        new_font = "Courier"

        if self.family.get() == "times":
            new_font = new_font + "times"
        else:
            new_font = new_font + "helvetica"

        if self.point_size.get() == "10":
            new_font = new_font + " 10"
        else:
            new_font = new_font + " 12"

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
      
        self.sample_label.config( font = new_font)

frame04 = MyFrame()
frame04.mainloop()