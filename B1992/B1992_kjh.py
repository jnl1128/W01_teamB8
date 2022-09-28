N = int(input())
image = [[0] * N for _ in range(N)]
for i in range(N):
    image[i] = [int(x) for x in input()]


result = ""

def solution(image, depth, s_row, s_col, e_row, e_col):
    global result
    if depth == 1:
        result += str(image[s_row][s_col])
        return
    color = data_check(image, s_row, s_col, e_row, e_col)
    if color != -1:
        result += str(color)
        return

    result += '('
    solution(image, depth//2, s_row, s_col, s_row+(e_row-s_row)//2, s_col+(e_col-s_col)//2)
    solution(image, depth//2, s_row, s_col+(e_col-s_col)//2, s_row+(e_row-s_row)//2, e_col)
    solution(image, depth//2, s_row+(e_row-s_row)//2, s_col, e_row, s_col+(e_col-s_col)//2)
    solution(image, depth//2, s_row+(e_row-s_row)//2, s_col+(e_col-s_col)//2, e_row, e_col)
    result += ')'


def data_check(image, s_row, s_col, e_row, e_col):
    color = image[e_row-1][e_col-1]
    for i in range(s_row, e_row):
        for j in range(s_col, e_col):
            if color != image[i][j]:
                return -1
    return color


solution(image, N, 0, 0, N, N)
print(*result, sep="")