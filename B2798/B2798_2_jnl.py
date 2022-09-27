# 블랙잭 #재귀
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

visited = [0 for _ in range(N)]
result = 0

def solution(depth, total):
    global result

    if total > M:
        return

    if depth == 3:
        result = max(result, total)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, total+cards[i])
            visited[i] = 0
    
solution(0, 0)
print('{}'.format(result))