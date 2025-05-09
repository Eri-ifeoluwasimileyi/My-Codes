import math
e_estimate = 0


for number in range(10):
    e_estimate += 1 / math.factorial(number)

print(f"Estimated value of e using 10 terms: {e_estimate:.10f}")