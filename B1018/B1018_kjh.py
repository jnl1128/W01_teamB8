n, m = map(int, input().split())
board = [''] * n
for i in range(n):
    board[i] = input()


def sol(board, n, m, size):
    min_count = m*n+1
    for r in range(n-size+1):
        for c in range(m-size+1):
            min_count = min(min_count, count(board, r, c, size))
    return min_count


def count(board, r, c, size):
    a = 'WBWBWBWB'
    b = 'BWBWBWBW'
    flag = 0
    case_a = 0
    case_b = 0
    for line in board[r:r+size]:
        for i in range(c, c+size):
            if line[i] != a[i-c]:
                if flag == 0:
                    case_a += 1
                else:
                    case_b += 1
            if line[i] != b[i-c]:
                if flag == 1:
                    case_a += 1
                else:
                    case_b += 1
        flag = (flag+1) % 2

    return case_a if case_a < case_b else case_b
            
            
print(sol(board, n, m, 8))