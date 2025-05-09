n = 0

while n < 1:
	n = int(input('Enter an integer: '))
		
	if n < 1:
		print('Please enter a number greater than 0')

for number in range(n, 0, -1):
	print(number)
print()
print('Blast off!')