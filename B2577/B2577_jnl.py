import sys
input = sys.stdin.readline
from collections import Counter

A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)
dictABC = Counter(ABC)

for digit in range(0, 10):
    if str(digit) in dictABC:
        print(dictABC[str(digit)])

    else:
        print(0)