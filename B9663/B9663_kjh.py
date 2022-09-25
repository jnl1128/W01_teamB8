import sys

N = int(sys.stdin.readline().rstrip())
visited_col = [0 for _ in range(N)]
visited_diagonal_1 = [0 for _ in range(N*2)]
visited_diagonal_2 = [0 for _ in range(N*2)]

count = 0

def solution(row, flag):
    global count
    if row == N:
        count += 1
        return
    for col in range(N//2, N//2+1) if (flag is True and row==0) else range(N//2) if row==0 else range(N):
        if visited_col[col] == 0 and visited_diagonal_1[row+col] == 0 and visited_diagonal_2[row-col+N] == 0:
            visited_col[col] = 1
            visited_diagonal_1[row+col] = 1
            visited_diagonal_2[row-col+N] = 1

            solution(row+1, flag)

            visited_col[col] = 0
            visited_diagonal_1[row+col] = 0
            visited_diagonal_2[row-col+N] = 0


solution(0, False)
count *= 2
if N % 2 == 1:
    solution(0, True)

sys.stdout.write(f'{count}')
