"""This is the get quote program"""
from cleaningQuote import quote

myQuote = quote()
hst = "13%"
get_sqft = int(input("Enter the square footage of your home (ex. 1200): "))
get_bath = int(input("Enter the number of bathrooms in your home (ex. 2): "))
get_bed = int(input("Enter the number of bedrooms in your home (ex. 2): "))
get_basement = input("Do you require your basement to be cleaned ('yes' or 'no'): ")
get_initial = input("Have you had our cleaning services before ('yes' or 'no'): ")
get_frequnecy = input("How often would you like your home cleaned ('one time', 'weekly', 'biweekly' or 'monthly'): ")
myQuote.set_baseprice(get_sqft)
myQuote.set_bathroomprice(get_bath)
myQuote.set_bedroomprice(get_bed)
myQuote.set_basementprice(get_basement, get_sqft)
myQuote.set_initialvisit(get_initial)
myQuote.set_discount(get_frequnecy)

if get_initial == "no":
	print("The price for your initial visit will be: $", end="\r")
	myQuote.print_initialquote()
else:
	print("The price for your first visit will be: $", end="\r")
	myQuote.print_initialquote()
if get_frequnecy == "weekly":
	print("The price for your ongoing weekly visits will be: $", end="\r")
	myQuote.print_discountquote()
elif get_frequnecy == "biweekly":
	print("The price for your ongoing biweekly visits will be: $", end="\r")
	myQuote.print_discountquote()
elif get_frequnecy == "monthly":
	print("The price for your ongoing monthly visits will be: $", end="\r")
	myQuote.print_discountquote()
print("NOTE: All quoted prices are subject to HST currently ", hst)