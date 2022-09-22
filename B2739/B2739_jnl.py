import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, 10):
    print('{n1} * {n2} = {n3}' .format(n1=N, n2=i, n3=N*i))