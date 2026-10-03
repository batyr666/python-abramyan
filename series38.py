K = 3

sets = [[1, 3, 5, 8, 0], [9, 6, 2, -1, 0], [2, 5, 3, 7, 0]]

for a in sets:
    inc = all(a[i] < a[i + 1] for i in range(len(a) - 2))
    dec = all(a[i] > a[i + 1] for i in range(len(a) - 2))
    print(1 if inc else -1 if dec else 0)
