import sys

n, m = map(int, input().split())

used = [0] * (n+1)

def solution(depth, pre, result):
    if depth == m:
        sys.stdout.write(result+"\n")
        return
    for i in range(pre, n+1):
        solution(depth+1, i, result + str(i) + ' ')

solution(0, 1, '')