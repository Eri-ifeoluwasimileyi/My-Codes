largest  = -29903373
smallest = 200039936


for number in range(1, 11):

	number = int(input('Enter a number: '))

	if number > largest:
		largest = number

	if number < smallest:
		smallest = number

print('The largest number is:', largest)

print('The smallest number is:', smallest)