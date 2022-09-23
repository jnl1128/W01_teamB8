import sys
input = sys.stdin.readline

N = int(input())
if N <= 1:
    print(1)
else:
    result = 1
    for i in range(2, N+1):
        result *= i
    print(result)