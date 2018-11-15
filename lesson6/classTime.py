"""Creating a time class"""

class Time:
	"""Blueprint for a Time object"""
	def __init__(self):
		"""The initial defining fuction of the class Time"""
		self.__hour = 0
		self.__minute = 0
		self.__second = 0

	def tick(self):
		self.__second = self.__second + 1
		if ( self.__second == 60 ):
			self.__second = 0
			self.__minute = self.__minute + 1
			if ( self.__minute == 60 ):
				self.__minute = 0
				self.__hour = self.__hour + 1
				if ( self.__hour == 24 ):
					self.__hour = 0


	def set_time(self, hour, minute, second):
		"""This function sets the time object variables"""
		self.set_hour(hour)
		self.set_minute(minute)
		self.set_second(second)

	def print_time(self):
		"""This function will print out time input received in a time format hh:mm:ss"""
		print (self.__hour, ":", self.__minute, ":", self.__second)

	def set_hour(self, hour):
		"""This function is to define the hour variable so that it cannot be accessed directly"""
		if (hour >= 0 and hour <= 23):
			self.__hour = hour
		else:
			self.__hour = 0

	def set_minute(self, minute):
		"""This function is to define the minute variable so that it cannot be accessed directly"""
		if (minute >= 0 and minute <= 59):
			self.__minute = minute
		else:
			self.__minute = 0

	def set_second(self, second):
		"""This function is to define the second variable so that it cannot be accessed directly"""
		if (second >= 0 and second <= 59):
			self.__second = second
		else:
			self.__second = 0

	def get_hour(self):
		"""This function returns the set hour variable to the program"""
		return self.__hour

	def get_minute(self):
		"""This function returns the set minute variable to the program"""
		return self.__minute

	def get_second(self):
		"""This function returns the set second variable to the program"""
		return self.__second