import sys

n = int(sys.stdin.readline().rstrip())
w = [[0 for __ in range(n)] for _ in range(n)]
for i in range(n):
    w[i] = list(map(int, sys.stdin.readline().split()))

visited = [0 for _ in range(n)]

min_sum = 9876543210
def solution(depth, sum, start):
    global min_sum
    global visited

    if sum > min_sum:
        return

    if depth == n-1:
        if w[start][0] != 0:
            min_sum = min(min_sum, sum + w[start][0])
        return
    
    for i in range(1, n):
        if visited[i] == 0 and w[start][i] != 0:
            visited[i] = 1
            solution(depth+1, sum + w[start][i], i)
            visited[i] = 0


solution(0, 0, 0)
sys.stdout.write(f'{min_sum}')