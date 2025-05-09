value = int(input('Enter an interger (-1 to break): '))

while value -1:

	for score in range(2):

		value = int(input('Enter an interger (-1 to break): '))

		print('You entered:', value)
	
		if value == -1:
			break
	else: 
		print('The loop terminated without executing the break')	
