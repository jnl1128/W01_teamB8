result = [0 for _ in range(10)]
a, b, c = map(int, open(0))
for num in str(a*b*c):
    result[int(num)] += 1