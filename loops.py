list = ["host1","host2","host3","host4"]
counter = 0
max_index = len(list) - 1
# While Loop
print("While loop")
while counter <= max_index:
   word = list[counter]
   print(word + "!")
   counter = counter + 1 
# For loop
print("For loop")
for word in list:
	print(word+"!")

# for loop to print code multiple times
for i in range(20):
	print("hello!")
# same output as above without a loop, if we just want strings repeated so many times
print("-" * 30)
print("hello!\n" * 5)

# print even numbers up to 20
for i in range(49, 0, -1):
	print(i)

number = 1
answer = 'n'
while answer == 'y':
         print (number)
         number = number + 1
         answer = input(
                "Do you want the next number? ")

num_of_nums = eval(input(
         "How many numbers do you want to average? "))

sum = 0.0
for count in range (num_of_nums):
         value = eval(input("Enter a value: "))
         sum = sum + value

average = sum / num_of_nums
print ("The average is:", average)