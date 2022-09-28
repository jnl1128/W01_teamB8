#NM과 K(1)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split(' '))
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split(' '))))
maxResult = -10000 * K

def check(r, c):
    if r -1 >= 0:
        if visited[r-1][c] == 1:
            return False
    if r+1 < N:
        if visited[r+1][c] == 1:
            return False
    if c-1 >= 0:
        if visited[r][c-1] == 1:
            return False
    if c+1 < M:
        if visited[r][c+1] == 1:
            return False
    return True


def solution(depth, total):
    global maxResult
    if depth == K:
        maxResult = max(maxResult, total)
        return
    if total + 10000 * (K-depth) < maxResult:
        return
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 1 and check(i, j) :
                visited[i][j] = 1
                solution(depth+1, total+matrix[i][j])
                visited[i][j] = 0

                

visited= [[0]*M for _ in range(N)]
solution(0, 0)
print(maxResult)
