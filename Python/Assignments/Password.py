password = str(input('Enter the password: '))
length = len(password)

if length > 0 and length < 8:
	print('very weak')

elif length == 8:
	print('weak')

elif length > 8 and length <= 16:
	print('strong')

elif length > 16:
	print('very strong')

else:
	print('Password is needed, try again!')
	