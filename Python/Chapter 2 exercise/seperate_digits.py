number = int(input("Enter a number:"))

 	
digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0
digit5 = 0
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