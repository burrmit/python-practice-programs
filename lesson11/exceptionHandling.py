try:
    #age = eval(input("enter your age: "))
    ten_years = age + 10
    print("In 10 years you will be: ", ten_years)
except NameError:
    print("NameError: You must enter a number for your age")
except SyntaxError:
    print("SyntaxError: You must enter a number for your age")

print("Have a nice day, Goodbye!")

print("~" * 40)

try:
    #age = eval(input("enter your age: "))
    ten_years = age + 10
    print("In 10 years you will be: ", ten_years)
except (NameError, SyntaxError):
    print("You must enter a number for your age")
    
print("Have a nice day, Goodbye!")

print("~" * 40)

try:
    #age = eval(input("enter your age: "))
    ten_years = age + 10
    print("In 10 years you will be: ", ten_years)
except Exception:
    print("You must enter a number for your age")
    
print("Have a nice day, Goodbye!")

print("~" * 40)

try:
    #age = eval(input("enter your age: "))
    ten_years = age + 10
    print("In 10 years you will be: ", ten_years)
except NameError:
    print("NameError: You must enter a number for your age")
except SyntaxError:
    print("SyntaxError: You must enter a number for your age")
except Exception:
    print("GeneralException: You must enter a number for your age")
    
print("Have a nice day, Goodbye!")

print("~" * 40)

try:
   my_list = [0, 1, 2] 
   print (my_list [4]) 
except IndexError as ie:
   print (ie)


print("~" * 40)

try:
   user_num = eval( input("Please enter a number: ") )
   result = 10 / user_num
except (NameError, SyntaxError):
   print ("The value you entered was not a number")
except ZeroDivisionError:
   print ("You cannot divide by zero")
else:
   print ("The result of dividing 10 by your number is", result)

print("~" * 40)

try:
   infile = open('data.txt', 'r')
   try:
       value = infile.readline()
       number = int(value)
       print (number)
   finally:
       infile.close()
       print ("the data file was closed")
except IOError as io:
   print ("Could not open file:", io.filename)
except ValueError:
   print ("Could not convert", value, "to a number")
