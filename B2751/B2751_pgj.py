import sys

a = int(input())

arr = []
for i in range(a):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()

for i in range(len(arr)):
    print(arr[i])