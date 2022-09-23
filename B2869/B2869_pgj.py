A, B, V = input().split()
A = int(A)
B = int(B)
V = int(V)

H = V - A
result = H // (A-B)

if(H % (A-B) == 0):
    result += 1
else:
    result += 2
print(result)
