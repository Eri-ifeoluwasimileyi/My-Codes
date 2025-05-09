total_miles_driven = float(0)
total_gallons_used = float(0)


gallons_used = float(input('Enter thr gallons used (-1 to end): '))

while gallons_used != -1:

	

	miles_driven = float(input('Enter the miles driven: '))

	miles_per_gallon = miles_driven / gallons_used
	
	print('The miles/gallon for this tank was ', miles_per_gallon)


	total_miles_driven += miles_driven

	total_gallons_used += gallons_used

	gallons_used = float(input('Enter thr gallons used (-1 to end): '))


average = total_miles_driven / total_gallons_used
	
print('The overall average miles/gallon was ', average)