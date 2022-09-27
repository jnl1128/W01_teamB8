# 하노이 탑 이동 순서
import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print('{} {}\n'.format(a, c))
        return
    hanoi(n-1, a, c , b)
    hanoi (1, a, b, c)
    hanoi(n-1, b, a, c)

print('{}\n'.format(pow(2, N)-1))
hanoi(N, 1, 2, 3)

