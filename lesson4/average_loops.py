num_of_nums = eval(input(
         "How many numbers do you want to average? "))

sum = 0.0
for count in range (num_of_nums, 0, -1):
         value = eval(input("Enter a value: "))
         sum = sum + value

average = sum / num_of_nums
print ("The average is:", average)
