a, b = input().split()
a = int(a)
b = int(b)
a = a // 100 + ((a // 10) % 10) * 10 + (a % 10)*100
b = b // 100 + ((b // 10) % 10) * 10 + (b % 10) *100

if (a > b):
    print(a)
else:
    print(b)