import sys
input = sys.stdin.readline

N, X = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

result = [num for num in arr if num < X]

for num in result:
    print(num, end=' ')