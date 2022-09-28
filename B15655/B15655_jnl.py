#N과M(6)
import sys
input = sys.stdin.readline
N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()
visited = [0 for _ in range(N)]

def solution(depth, stack, start):
    if depth == M:
        print(*stack)
        return

    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, stack+[arr[i]], i)
            visited[i] = 0

solution(0, [], 0) 