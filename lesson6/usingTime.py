"""This python script will make use of the Time module"""
from classTime import Time

# First Time object
myTime1 = Time()
myTime1.hour = 47
myTime1.print_time()
myTime1.set_hour(50)
myTime1.print_time()
myTime1.set_time(1, 2, 3)

# Secondary Time object
myTime2 = Time()
myTime2.set_time(12, 53, 26)

print ("My two time objects are now storing:")
myTime1.print_time()
myTime2.print_time()

print(myTime1._Time__second)
print("Here is the Time class documentation:")
print("-"*37)
print(myTime1.__doc__)
print(myTime1.set_time.__doc__)
print(myTime1.print_time.__doc__)
print("This attribute will give you the class from which the object is pulling:")
print(myTime2.__class__)