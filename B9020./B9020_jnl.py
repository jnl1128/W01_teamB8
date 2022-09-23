import sys, math
input = sys.stdin.readline

def checkPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())

    for i in range(n//2, 1, -1):
        if checkPrime(i) and checkPrime(n-i):
            print(i, n-i)
            break