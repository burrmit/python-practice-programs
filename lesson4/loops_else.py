for number in range(1, 11):
         if number == 4:
                   break
         print (number)
else:
         print ("Exited normally")

for number in range(1, 11):
         if number == 4:
                   continue
         print (number)
else:
         print ("Exited normally")

phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
         if phrase [index] == letter:
                   print ("We found the letter '",letter,"' in your phrase")
                   break
else:
         print ("Your letter wasn't found")
