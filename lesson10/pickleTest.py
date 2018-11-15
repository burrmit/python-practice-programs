import pickle

outfile = open('data.txt', 'wb')
letters = ['a', 'b', 'c']
pickled_letters = pickle.dumps(letters)
print("Pickled letters stored as a string variable")
print(pickled_letters)

pickle.dump(letters, outfile)
outfile.close()

print("~" * 40)
print("Unpickled letters stored as a string variable")
unpickled_letters = pickle.loads(pickled_letters)
print (unpickled_letters)
print("~" * 40)
print("Unpickled letters from the stored data.txt file")
infile = open('data.txt', 'rb')
file_data = pickle.load(infile)
infile.close()
print(file_data)
