a = [1, 5, 2, 6, 6, 3]

res = 0

for i in range(1, len(a) - 1):
    if (a[i] - a[i - 1]) * (a[i] - a[i + 1]) <= 0:
        result = i + 1
        break
print(result)
