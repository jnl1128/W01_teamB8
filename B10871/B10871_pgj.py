a, b = input().split()
a = int(a)
b = int(b)

X = [a]
X = input().split()

for i in range(a):
    if(int(X[i]) < b):
        print(X[i], end=" ")