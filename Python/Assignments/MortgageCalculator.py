principalAmount = float(input('Enter the principal amount: '))

annualInterestRate = float(input('Enter the annual interest rate: '))

numberOfYears = float(input('Enter the duration in Years: '))



monthlyInterestRate = (annualInterestRate / 100) / 12
numberOfMonths = numberOfYears * 12


paymentCalculation = monthlyInterestRate *(1 + monthlyInterestRate)** numberOfMonths  

paymentCalculation2 = (1 + monthlyInterestRate)** numberOfMonths - 1

mortgageRepayment = principalAmount * (paymentCalculation/paymentCalculation2)


print('Your monthly payment is $%.2f' % mortgageRepayment)  
