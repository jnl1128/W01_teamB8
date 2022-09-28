import sys

n, m = map(int, sys.stdin.readline().split())

def solution(depth, pre, result):
    if depth == m:
        sys.stdout.write(result+"\n")
        return
    for i in range(pre, n+1):
        solution(depth+1, i, result + str(i) + ' ')

solution(0, 1, '')