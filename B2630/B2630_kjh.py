from re import L
import sys
n = int(sys.stdin.readline().rstrip())
paper = [0] * n
for i in range(n):
    paper[i] = list(map(int, sys.stdin.readline().split()))

count = [0, 0]

def solution(N, paper, start_row, start_col, end_row, end_col):
    global count
    if N == 1:
        count[paper[start_row][start_col]] += 1
        return
    
    color = check(paper, start_row, start_col, end_row, end_col)
    if color != -1:
        count[color] += 1
        return

    solution(N//2, paper, start_row, start_col, start_row+N//2, start_col+N//2)
    solution(N//2, paper, start_row, start_col+N//2, start_row+N//2, end_col)
    solution(N//2, paper, start_row+N//2, start_col, end_row, start_col+N//2)
    solution(N//2, paper, start_row+N//2, start_col+N//2, end_row, end_col)


def check(paper, start_row, start_col, end_row, end_col):
    color = paper[end_row-1][end_col-1]
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if color != paper[i][j]:
                return -1
    return color

solution(n, paper, 0, 0, n, n)

print(f'{count[0]}\n{count[1]}')