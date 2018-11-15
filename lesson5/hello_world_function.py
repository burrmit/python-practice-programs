def print_welcome():
	"""This function prints two lines of text"""
	print("Welcome to the world of functions")
	print("Hello World")

def print_value(value):
	"""This function prints out the value that is passed to it"""
	print("This is the value you passed: ", value)

def change_value(value):
	"""This function is to test changing the variable value in the function"""
	print("Inside, value is: ", value)
	value = 1
	print("Inside, value is changed to: ", value)
	global number
	number = 1

def square(num):
	"""This function will get you the square root of the number passed to it"""
	result = num * num
	return result

def prompt_user(prompt, num_tries = 2):
    """This function prompts the user a certain number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)


print("-" * 30) 
print_welcome()

print("-" * 30)
print_value("first value")
print_value("number 5")
print_value("20")
name = "My name"
print_value(name)

print("-" * 30)
number = 30
print("Outside, value of number is: ", number)
change_value(number)
print("Outside, value of number is now: ", number)

print("-" * 30)
for i in range(1,11):
	print(square(i))

print(square(22))

print("-" * 30)
#prompt_user("Enter yes or no: ")
prompt_user("Enter yes or no: ", 4)