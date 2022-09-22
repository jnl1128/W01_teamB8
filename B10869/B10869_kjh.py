import sys

a, b = map(int, sys.stdin.readline().split())
print(f'{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}')