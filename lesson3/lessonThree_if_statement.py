age = 32
if age != 10:
	print(age)
print("how is that?")

print("-" * 30)

name = "me"
if name == "me":
	print("the same")

print("-" * 30)

letter = "C"
print("The value of var letter is: ", letter)
if letter < "D":
    print ("'letter' is less than D")

if letter > "B":
    print ("'letter' is greater than B")

letter = "C"
if letter < "a":
    print ("'letter' is less than a")

print("-" * 30)

# age = int(input("Please enter your age: "))
if age >= 18:
   print ("Congratulations!")
   print ("You are old enough to vote.")
else:
   print ("I'm sorry.")
   print ("You are not old enough to vote.")

print("-" * 30)

# year = int(input("Enter year: "))
year = 3
if year == 1:
   print ("Freshman")
if year == 2:
   print ("Sophomore")
if year == 3:
   print ("Junior")
if year == 4:
   print ("Senior")

if year == 1:
   print ("Freshman")
else:
   if year == 2:
      print ("Sophomore")
   else:
      if year == 3:
         print ("Junior")
      else:
      	if year == 4:
      		print ("Senior")

if year == 1:
	print("Freshman")
elif year == 2:
	print("Sophomore")
elif year == 3:
	print("Junior")
elif year == 4:
	print("Senior")
else:
   print ("Not a valid year")

print("-" * 30)

# age = eval(input("How old are you? "))
# registered = input("Are you registered? (y/n) ")
registered = "y"
if age >= 18:
    if registered == "y":
         print ("You are ready to vote!")
    else:
    	 print ("You are old enough, but need to register to vote!")
else:
    print ("You are not ready to vote.")

if age >= 18 and registered == "y":
    print ("You are ready to vote!")
else:
    print ("You are not ready to vote.")

print("-" * 30)

rate = eval(input("What is your hourly wage? "))
hours = eval(input("How many hours did you work? "))

if hours < 40:
    pay = hours * rate
else:
    pay = hours * rate
    overtimeHours = hours - 40
    overtimePay = overtimeHours * (rate * 0.5)
    pay = pay + overtimePay

print ("Your weekly pay is: ", pay)