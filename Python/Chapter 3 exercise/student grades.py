passes = 0
failures = 0

result = int(input('Enter the result: '))

while True:
	
	if result < 1 or result > 2:
		print('Enter a valid input.')

		result = int(input('Enter the result: '))

	if result > 0 and result < 3:
		break


for student in range(1, 11):
	result = int(input('Enter the result: '))


	if result == 1:
		passes = passes + 1
	else:
		failures = failures + 1


print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
	print('Bonus to instructor')

		