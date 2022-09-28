#N과M(6)
import sys
input = sys.stdin.readline
N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

visited = [0 for _ in range(N)]
result = []

def solution(depth, stack, start):
    if depth == M:
        stack.sort()
        if stack not in result:
            result.append(stack)
        return

    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, stack+[arr[i]], i)
            visited[i] = 0

solution(0, [], 0) 
result.sort()
for elem in result:
    print(*elem, sep =' ')