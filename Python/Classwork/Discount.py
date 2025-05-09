total_spending = float(input('Enter how much you will like to purcase: '))

discount_5 = (total_spending * 5) / 100

discount_10 = (total_spending * 10) / 100

discount_20 = (total_spending * 20) / 100

balance_after_5 = total_spending - discount_5

balance_after_10 = total_spending - discount_10

balance_after_20 = total_spending - discount_20


if total_spending >= 1000 or total_spending <= 10000:
	print(f'Your discount is  {discount_5:,.2f} and your price after discount is {balance_after_5:,.2f}') 

elif total_spending > 10000 or total_spending <= 50000:
	print(f'Your discount is {discount_10:,.2f} and your price after discount is {balance_after_10:,.2f}') 

elif total_spending > 50000:
	print('Your discount is {discount_20:,.2f} and your price after discount is {balance_after_20:,.2f}') 

