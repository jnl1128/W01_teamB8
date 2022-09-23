import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))

maxV = max(arr)
index = arr.index(maxV)
print(maxV, index+1, sep='\n')