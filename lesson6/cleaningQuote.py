"""Cleaning Quote Class"""

class quote:
	"""Class quote to process estimated costs"""
	def __init__(self):
		self.__base_price = 0
		self.__bathroom_price = 0
		self.__bedroom_price = 0
		self.__basement_price = 0
		self.__initial_quote = 0.10
		self.__weekly_discount = 0.20
		self.__biweekly_discount = 0.15
		self.__monthly_discount = 0.10

	def set_baseprice(self, sqft):
		if sqft < 501:
			self.__base_price = 30.0
		elif sqft > 500 and sqft < 1001:
			self.__base_price = 40.0
		elif sqft > 1000 and sqft < 1501:
			self.__base_price = 50.0
		elif sqft > 1500 and sqft < 2001:
			self.__base_price = 60.0
		elif sqft > 2000 and sqft < 2501:
			self.__base_price = 70.0
		elif sqft > 2500 and sqft < 3001:
			self.__base_price = 80.0
		elif sqft > 3000 and sqft < 3501:
			self.__base_price = 90.0
		elif sqft > 3500 and sqft < 4001:
			self.__base_price = 100.0
		elif sqft > 4000:
			self.__base_price = 150.0

	def set_bathroomprice(self, bath):
		self.__bathroom_price = bath * 6

	def set_bedroomprice(self, bed):
		self.__bedroom_price = bed * 5

	def set_basementprice(self, basement, sqft):
		if basement == "yes" and sqft < 501:
			self.__basement_price = 5.0
		elif basement == "yes" and sqft > 500 and sqft < 1001:
			self.__basement_price = 8.0
		elif basement == "yes" and sqft > 1000 and sqft < 1501:
			self.__basement_price = 11.0
		elif basement == "yes" and sqft > 1500 and sqft < 2001:
			self.__basement_price = 14.0
		elif basement == "yes" and sqft > 2000 and sqft < 2501:
			self.__basement_price = 17.0
		elif basement == "yes" and sqft > 2500 and sqft < 3001:
			self.__basement_price = 20.0
		elif basement == "yes" and sqft > 3000 and sqft < 3501:
			self.__basement_price = 23.0
		elif basement == "yes" and sqft > 3500 and sqft < 4001:
			self.__basement_price = 26.0
		elif basement == "yes" and sqft > 4000:
			self.__basement_price = 29.0
		elif basement == "no":
			self.__basement_price = 0
		else:
			print("Basement answer requires either 'yes' or 'no'.")

	def set_initialvisit(self, initial):
		if initial == "no":
			self.__initial_quote = 0

	def set_discount(self, discount):
		if discount == "weekly":
			self.__discount = self.__weekly_discount
		elif discount == "biweekly":
			self.__discount = self.__biweekly_discount
		elif discount == "monthly":
			self.__discount = self.__monthly_discount
		else:
			self.__discount = 0

	def get_baseprice(self):
		return self.__base_price

	def get_bathroomprice(self):
		return self.__bathroom_price

	def get_bedroomprice(self):
		return self.__bedroom_price

	def get_basementprice(self):
		return self.__basement_price

	def get_initialvisit(self):
		return self.__initial_quote

	def get_discount(self):
		return self.__discount

	def get_initialquote(self):
		self.initial_quote = self.__base_price + self.__bathroom_price + self.__bedroom_price + self.__basement_price
		self.calinitial = self.initial_quote*self.__initial_quote
		self.final_initial_quote = float((self.initial_quote + self.calinitial) * 1.13)
		return self.final_initial_quote

	def get_discountquote(self):
		self.discount_quote = self.__base_price + self.__bathroom_price + self.__bedroom_price + self.__basement_price
		self.caldiscount = self.discount_quote*self.__discount
		self.final_discount_quote = float((self.discount_quote - self.caldiscount) * 1.13)
		return self.final_discount_quote

	def print_initialquote(self):
		self.get_initialquote()
		print("%.2f" % self.final_initial_quote)

	def print_discountquote(self):
		self.get_discountquote()
		print("%.2f" % self.final_discount_quote)