import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split(' '))

result = 1000
if x < result:
    result = x
if y < result:
    result = y
if (w-x) < result:
    result = (w-x)
if (h-y) < result:
    result = (h-y)

print(result)

