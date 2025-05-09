largest = -234567907
smallest = 234568908

sum_of_numbers = 0
product_of_numbers = 1
average_of_numbers = 0


for number in range(1, 5):
	
	number = int(input('Enter a number: '))

	sum_of_numbers = sum_of_numbers + number

	average_of_numbers = (sum_of_numbers) / number

	product_of_numbers = product_of_numbers * number
   


	if number > largest:
		largest = number

	if number < smallest:
		smallest = number



print('The sum of the number is:', sum_of_numbers)

print('The average of the number is:', average_of_numbers)

print('The product of the number is:', product_of_numbers)

print('The largest number is:', largest)

print('The smallest number is:', smallest)