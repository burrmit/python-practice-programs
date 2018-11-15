"""Creating a time class"""

class Time:
	"""Blueprint for a Time object"""
	def __init__(self):
		"""The initial defining fuction of the class Time"""
		self.__hour = 0
		self.__minute = 0
		self.__second = 0

	def set_time(self, hour, minute, second):
		"""This function sets the time object variables"""
		self.__hour = hour
		self.__minute = minute
		self.__second = second

	def print_time(self):
		"""This function will print out time input received in a time format hh:mm:ss"""
		print (self.__hour,":",self.__minute,":",self.__second)

	def set_hour(self, hour):
		"""This function is to define the hour variable so that it cannot be accessed directly"""
		self.__hour = hour

	def get_hour(self):
		"""This function returns the set hour variable to the program"""
		return self.__hour

	def set_minute(self, minute):
		"""This function is to define the minute variable so that it cannot be accessed directly"""
		self.__minute = minute

	def get_minute(self):
		"""This function returns the set minute variable to the program"""
		return self.__minute

	def set_second(self, second):
		"""This function is to define the second variable so that it cannot be accessed directly"""
		self.__second = second

	def get_second(self):
		"""This function returns the set second variable to the program"""
		return self.__second