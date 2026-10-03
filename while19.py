N = 123
res = 0

while N > 0:
    res = res * 10 + N % 10
    N //= 10

print(res)
