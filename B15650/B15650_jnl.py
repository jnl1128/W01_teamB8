#N과 M(2)
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = [i for i in range(1, N+1)]

visited = [0 for _ in range(N+1)]

def solution(depth, stack, start):
    if depth == M:
        print(*stack)
        return
    
    for i in range(start, N+1):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, stack+[arr[i-1]], i)
            visited[i] = 0

solution(0, [], 1)  