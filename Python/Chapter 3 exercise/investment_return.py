principal = 1000

annual_rate_of_return = 7 / 100



for years in range(1, 31):
	
	amount = principal * (1 + annual_rate_of_return)** (years)

	print('After year', years)
	print('The amount on the deposit at the end of the year is: $%.2f' % amount)



