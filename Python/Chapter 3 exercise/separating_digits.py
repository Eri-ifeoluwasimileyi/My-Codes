for number in range(1):

	number = int(input("Enter a number:"))
	remainder = 0



	if number < 10000 or number > 99999:
		print('ivalid input')
	
	if number > 10000 and number < 99999:
	
		digit1 = number % 10
		remainder = number // 10

		digit2 = remainder % 10
		remainder = remainder // 10

		digit3 = remainder % 10
		remainder = remainder // 10

		digit4 = remainder % 10
		remainder = remainder // 10

		digit5 = remainder % 10
		remainder = remainder // 10
	
print(digit5,'   ',digit4,'   ',digit3,'   ',digit2,'   ',digit1)