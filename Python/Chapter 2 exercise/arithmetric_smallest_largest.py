number1 = float(input("Enter first integer: "))
number2 = float(input("Enter second integer: "))
number3 = float(input("Enter third integer: "))

sumOfNumbers = number1 + number2 + number3
averageOfNumbers = (number1 + number2 + number3) / 3
productOfNumbers = number1 * number2 * number3
   
print('The sum of the number is: $%.2f' % sumOfNumbers)
print('The average of the number is: $%.2f' % averageOfNumbers)
print('The product of the number is: $%.2f' % productOfNumbers)


if number1 > number2 and number1 > number3:
	print(f"{number1} is the largest number")
	
if number2 > number1 and number2 > number3:
	print(f"{number2} is the largest number")
	
if number3 > number1 and number3 > number2:
	print(f"{number3} is the largest number")


	
if number1 < number2 and number1 < number3:
	print(f"{number1} is the smallest number")
	
if number2 < number1 and number2 < number3:
	print(f"{number2} is the smallest number")
	
if number3 < number1 and number3 < number2:
	print(f"{number3} is the smallest number")
	