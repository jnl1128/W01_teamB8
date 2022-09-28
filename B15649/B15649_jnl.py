#N과 M(1)
from audioop import reverse
import sys
input = sys.stdin.readline
# print = sys.stdout.write

N, M = map(int, input().split(' '))

arr = [i for i in range(1, N+1)]
visited = [0  for _ in range(N+1)]
result = []

def solution(depth, stack):
    if depth == M:
        # stack.sort(reverse=True)
        result.append(stack)
        return

    for i in range(1,N+1):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, stack+[arr[i-1]])
            visited[i] = 0

solution(0, [])
result.sort()
for elem in result:
    print(*elem, sep=' ')