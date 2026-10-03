N = 5
a = [1, 0, 2, 4, 6]
k = 0

for i in range(N - 1):
    if a[i] < a[i + 1]:
        print(a[i])
        k += 1

print("k:", k)
