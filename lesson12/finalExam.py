
value = 1
number = 2
if value == 0:
	if number == 1:
		print("We got it")
	else:
		print("The number isnt 1")
else:
	print("the value isnt 0")
	if number == 1:
		print("We got it")
	else:
		print("The number isnt 1")

my_list = ['1', '2']
my_list2 = ['3', '4']
my_list.extend(my_list2)
print(my_list)

my_dict = {"One": 1, "Two": 2}
print(my_dict.items())

outfile = open("data.txt", 'w')
colors = ['blue', 'white']
outfile.write("colors")
outfile.writelines(colors)
outfile.close( )	