import sys

n, m = map(int, sys.stdin.readline().split())

def solution(depth, result):
    if depth == m:
        sys.stdout.write(result+"\n")
        return
    for i in range(1, n+1):
        solution(depth+1, result + str(i) +' ')

solution(0, '')