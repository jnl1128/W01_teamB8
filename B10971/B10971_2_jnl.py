# 외판원 순회 2
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
routes = []
for _ in range(N):
    routes.append(list(map(int, input().split(' '))))

visited = [0 for _ in range(N)]

minWeight = 1000000 * N

def solution(depth, total, preIdx, startNode):
    global minWeight

    if depth == N-1:
        if routes[preIdx][startNode] != 0:
            total += routes[preIdx][startNode]
            minWeight = min(minWeight, total)
        return
    else:
        if total > minWeight:
            return

        for i in range(N):
            if visited[i] == 0 and routes[preIdx][i] != 0:
                visited[i] = 1
                solution(depth+1, total+routes[preIdx][i], i, startNode)
                visited[i] = 0

for i in range(N):  
    visited[i] = 1
    solution(0, 0, i, i)
    visited[i] = 0

print('{}'.format(minWeight))