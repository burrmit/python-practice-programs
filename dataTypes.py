# Data Types Examples

sample = [1, ["another", "list"], ("a", "tuple")]
print("sample = [1, ['another', 'list'], ('a', 'tuple')]")
print(sample)

mylist = ["List item 1", 2, 3.14]
print("mylist = ['List item 1', 2, 3.14]")
print(mylist)

mylist[0] = "List item 1 again" # We're changing the item.
print("mylist[0] = List item 1 again")
print(mylist)

mylist[-1] = 3.21 # Here, we refer to the last item.
print("mylist[-1] = 3.21")
print(mylist)

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
print("mydict = {'Key 1': 'Value 1', 2: 3, 'pi': 3.14}")
print(mydict)

mydict["pi"] = 3.15 # This is how you change dictionary values.
print("mydict['pi'] = 3.15")
print(mydict)

mytuple = (1, 2, 3)
print("mytuple = (1, 2, 3)")
print(mytuple)

myfunction = len
print(myfunction(mylist))
