purchase_price = float(input('Enter the purchase price: '))

change = round((1.00 - purchase_price) * 100)

quarters = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickels = change // 5
change = change % 5


pennies = change

print('Your change is:')

if nickels > 0:
	print(nickels, 'nickels')
	
if dimes > 0:
	print(dimes, 'dimes')

if quarters > 0:
	print(quarters, 'quarters')

if pennies > 0:
	print(pennies, 'pennies')



