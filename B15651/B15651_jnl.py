#N과 M(3)
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = [i for i in range(1, N+1)]

def solution(depth, stack):
    if depth == M:
        print(*stack)
        return
    
    for i in range(1, N+1):
        solution(depth+1, stack+[arr[i-1]])

solution(0, [])
