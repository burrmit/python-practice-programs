
days_of_the_week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']

for i in days_of_the_week:
	print(i, "\t", end="\r")

"""this prints out a line"""
print("-" * 30)

"""change a value in the list"""
days_of_the_week [0] = 'Sunday'
print(days_of_the_week)
for i in range(len(days_of_the_week)):
	print(days_of_the_week[i])

"""this prints out a line"""
print("-" * 30)

"""More stuff"""
print(days_of_the_week[2:5])

"""Storing different data types in a list"""
child1 = ['Ashton', 2, 5.5]
child2 = ['Adurey', 1, 2]
parent1 = ['Michelle', 31, 7]
parent2 = ['Mitchell', 32, 11]
print(child1[2])

family = [[child1], [child2], [parent1], [parent2]]
print(family)

"""this prints out a line"""
print("-" * 30)

"""Going to work on appending to lists"""
my_list = []
my_list.append(10)
print(my_list)
my_list.append('ten')
print(my_list)
my_list.extend([20, 'twenty'])
print(my_list)
my_list = my_list + [30, 'thirty']
print(my_list)
my_list.insert(3, 'hi there!')
print(my_list)
my_list.remove('hi there!')
print(my_list)

"""this prints out a line"""
print("-" * 30)

my_numbers = [43, 69, 1, 32, 57, 22, 49, 11, 7]
print(my_numbers)
print(max(my_numbers))
my_numbers.reverse()
print(my_numbers)
my_numbers.sort()
print(my_numbers)

