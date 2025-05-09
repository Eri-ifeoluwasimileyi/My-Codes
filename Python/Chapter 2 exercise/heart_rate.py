age = int(input('Enter your age: '))

maximum_heart_rate = 220 - age

minimum_range = (maximum_heart_rate * 50) // 100

maximum_range = (maximum_heart_rate * 85) // 100

print('The maximum heart rate is', maximum_heart_rate)
print(f"The range is {minimum_range} - {maximum_range}")


