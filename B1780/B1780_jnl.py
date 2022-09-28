# 종이의 개수
import sys
N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split(' '))))

cnt = [0 for _ in range(3)]

def solution(width, r, c):

    if width == 1:
        if matrix[r][c] == -1:
            cnt[0]+= 1
        elif matrix[r][c] == 0:
            cnt[1]+= 1
        else:
            cnt[2]+= 1
        return

    color = matrix[r][c]
    for i in range(r, r+width):
        for j in range(c, c+width):
            if color != matrix[i][j]:
                nWidth = width//3
                solution(nWidth, r, c)
                solution(nWidth, r, c+nWidth)
                solution(nWidth, r, c+nWidth*2)

                solution(nWidth, r+nWidth, c)
                solution(nWidth, r+nWidth, c+nWidth)
                solution(nWidth, r+nWidth, c+nWidth*2)

                solution(nWidth, r+nWidth*2, c)
                solution(nWidth, r+nWidth*2, c+nWidth)
                solution(nWidth, r+nWidth*2, c+nWidth*2)
                return
    
    if color == -1:
        cnt[0] += 1
    elif color == 0:
        cnt[1] += 1
    else:
        cnt[2] += 1

solution(N, 0, 0)
# print(cnt[0], cnt[1], cnt[2], sep='\n')
sys.stdout.write('{} {} {}'.format(cnt[0], cnt[1], cnt[2]))