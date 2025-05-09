number1 = float(input('Enter first integer: '))

number2 = float(input('Enter second integer: '))

number3 = float(input('Enter third integer: '))


if number1 > number2 and number1 > number3:
	largest_number = number1

	if number2 > number3:
		second_largest = number2
		
	if number3 > number2:
		second_largest = number3
		
	
if number2 > number1 and number2 > number3:
	largest_number = number2
		
	if number1 > number3:
		second_largest = number1
	
	if number3 > number1:
		second_largest = number3
	
if number3 > number1 and number3 > number2:
	largest_number = number3
	
	if number1 > number2:
		second_largest = number1
	
	if number2 > number1:
		second_largest = number2
	



if number1 < number2 and number1 < number3: 
	smallest_number = number1
	
if number2 < number1 and number2 < number3:
	smallest_number = number2
		
if number3 < number1 and number3 < number2:
	smallest_number = number3


print(f'{smallest_number:.2f} {second_largest:.2f} {largest_number:.2f}')