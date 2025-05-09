number= int(input("Enter an interger: "))

 
firstNumber = number
remNumber = 0
reversedNumber = 0

while number != 0: 
	
	remNumber = number % 10
	reversedNumber = reversedNumber * 10 + remNumber
	number = number // 10
	

if firstNumber == reversedNumber:
		 print(firstNumber, 'is a palindrome')

if firstNumber != reversedNumber:
		print(firstNumber, 'is not a palindrome')





