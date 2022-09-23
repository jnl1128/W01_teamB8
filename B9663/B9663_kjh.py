import sys

n = int(sys.stdin.readline().rstrip())
v_col = [0 for _ in range(n)]
v_diagonal_1 = [0 for _ in range(n*2)]
v_diagonal_2 = [0 for _ in range(n*2)]
count = 0


def solution(row, flag):
    global count
    if row == n:
        count += 1
        return
    for col in range(n//2 if flag and row==0 else n):
        if v_col[col] == 0 and v_diagonal_1[row+col] == 0 and v_diagonal_2[row-col+n] == 0:
            v_col[col] = 1
            v_diagonal_1[row+col] = 1
            v_diagonal_2[row-col+n] = 1

            solution(row+1, flag)

            v_col[col] = 0
            v_diagonal_1[row+col] = 0
            v_diagonal_2[row-col+n] = 0


if n % 2 == 0:
    solution(0, True)
    count *= 2
else:
    solution(0, False)
sys.stdout.write(f'{count}')