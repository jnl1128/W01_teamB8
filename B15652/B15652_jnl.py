#N과M(4)
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = [i for i in range(1, N+1)]
result = []

def solution(depth, stack, start):
    if depth == M:
        stack.sort()
        if stack not in result:
            result.append(stack)
        return
    # 범위 조정!
    # 자신과 같거나 자신보다 큰 수만 뒤에 붙이면 되니까
    for i in range(start, N):
        solution(depth+1, stack+[arr[i-1]], i)

solution(0, [], 0)
result.sort()
for elem in result:
    print(*elem, sep=' ')