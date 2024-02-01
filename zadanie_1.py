a = [1, 2, 2, 1, 6, 4, 7, 8, 6, 5]

result = [a[i] for i in range(1, len(a)) if a[i] > a[i - 1]]

print(result)
