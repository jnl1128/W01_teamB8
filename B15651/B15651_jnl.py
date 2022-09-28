#N과 M(3)
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = [i for i in range(1, N+1)]
result = []

def solution(depth, stack):
    if depth == M:
        result.append(stack)
        return
    
    for i in range(N):
        solution(depth+1, stack+[arr[i-1]])

solution(0, [])
result.sort()
for elem in result:
    print(*elem, sep=' ')