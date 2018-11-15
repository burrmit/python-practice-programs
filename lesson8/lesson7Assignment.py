"""Lesson 7 assignment program"""

users_list = []
while True:
	user_input = eval(input("Please enter a number to be averaged: (-999 quits)"))
	if user_input != -999:
		users_list.append(user_input)
	else:
		break


list_length = len(users_list)
if list_length == 0:
	print("No values were entered!")
else:
	print("Using the following list of numbers: ", users_list)
	total_of_list = 0
	for i in users_list:
		total_of_list = total_of_list + i
	average = total_of_list / list_length
	print("The average is: ", average)
