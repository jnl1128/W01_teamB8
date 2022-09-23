import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num, string = input().split(' ')
    num = int(num)
    arr = list(string[:-1])
    for value in arr:
        print(value*num, end='')
    print('')
