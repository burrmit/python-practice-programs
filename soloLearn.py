list = ["host1","host2","host3","host4"]
counter = 0
max_index = len(list) - 1
print("While loop")
while counter <= max_index:
   word = list[counter]
   print(word + "!")
   counter = counter + 1 
print("For loop")
for word in list:
	print(word+"!")