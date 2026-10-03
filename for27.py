from math import asin

x = 0.5
N = 100

res = x

numerator = 1
denominator = 1

for i in range(1, N + 1):
    numerator *= 2 * i - 1
    denominator *= 2 * i

    res += (x ** (2 * i + 1) * numerator) / (denominator * (2 * i + 1))

print("res:", res)
print("arcsin:", asin(x))
