import sys, math
input = sys.stdin.readline

N = int(input())
arr = map(int, input().split(' '))

def checkPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

cnt = 0
for num in arr:
    if num == 1:
        continue
    elif num == 2:
        cnt += 1
        continue
    if checkPrime(num):
        cnt += 1
    
print(cnt)