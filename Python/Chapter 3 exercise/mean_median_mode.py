import statistics

grade = [9, 11, 17, 22, 22, 22, 34, 34, 40]

mean = statistics.mean(grade)

median = statistics.median(grade)

mode = statistics.mode(grade)


print('The mean of the grades is:', mean)
print('The median of the grades is:', median)
print('The mode of the grades is:', mode)




"""
The value 34 was not record
only 22 was recorded as the number which appear most
the error is an StatisticsError
"""