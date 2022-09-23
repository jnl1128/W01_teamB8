import sys
input = sys.stdin.readline

N = int(input())

numArr = [0] * 10001

for _ in range(N):
    idx = int(input())
    numArr[idx] += 1
    
for idx, num in enumerate(numArr):
    if num > 0:
        for _ in range(num):
            print(idx)