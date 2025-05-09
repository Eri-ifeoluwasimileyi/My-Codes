number = int(input('Enter a number: '))

counter = 0
answer = 1

	
while(counter < number) :
	
	answer = answer * (number - counter)
	
	counter = counter + 1

	

print('The Answer is:', answer)