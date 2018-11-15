

my_dictionary = { }

days_in_month = { 'Jan' : 31,
	'Feb' : 28,
	'Mar': 31,
	'Apr': 30,
	'May': 31,
	'Jun': 30,
	'Jul': 31,
	'Aug': 31}

print(days_in_month)

print(days_in_month.keys())
print(days_in_month.values())
print(days_in_month.items())
print("-" * 30)
'Mar' in days_in_month
days_in_month ['Test'] = 30
print(days_in_month['Test'])
days_in_month ['Test'] = 20
print(days_in_month['Test'])
days_in_month2 = {	'Sep': 30,
	'Oct': 31,
	'Nov': 30,
	'Dec': 31}
print(days_in_month2.items())
days_in_month.update(days_in_month2)
print(days_in_month.items())

print(days_in_month.get('January', 'January is not present in the dictionary'))

del days_in_month ['Test']
print(days_in_month.keys())
days_in_month.clear()
print(days_in_month)
del days_in_month2

