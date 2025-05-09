binary = int(input('Enter a binary number: '))

decimal_point = 0
positional_value = 0

while binary > 0:
	number = binary % 10

	decimal_point = decimal_point + number * (2 ** positional_value)
	binary = binary // 10
	positional_value = positional_value + 1
	

print('The decimal equivalent of the binary number is:', decimal_point)