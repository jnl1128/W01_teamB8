import sys
input = sys.stdin.readline

N = int(input())
# 현재 행에서 놓을 수 있는 col이 어디인지
# -> 이미 사용한 col이 무엇인지 알려주는 역할
v_col = [0 for _ in range(N)]
# 둘 수 없는 대각선1 정보
v_dia1 = [0 for _ in range((N)*2)]
# 둘 수 없는 대각선2 정보
v_dia2 = [0 for _ in range((N)*2)]

cnt = 0
def solution(depth, flag):
    global cnt 

    if depth == N:
        cnt += 1
        return

    if flag == True:
        for i in range(N//2):
            if v_col[i] == 0 and v_dia1[(depth - i +N)] == 0  and v_dia2[(depth + i )] == 0:
                v_col[i] = 1
                v_dia1[depth-i+N] = 1
                v_dia2[depth+i] = 1

                solution(depth+1, False)

                v_col[i] = 0
                v_dia1[depth-i+N] = 0
                v_dia2[depth+i] = 0

    else:
        for i in range(N):
            # 퀸을 둘 수 있는 곳인지 
            if v_col[i] == 0 and v_dia1[(depth - i +N)] == 0  and v_dia2[(depth + i )] == 0:
                v_col[i] = 1
                v_dia1[depth-i+N] = 1
                v_dia2[depth+i] = 1

                solution(depth+1, False)

                v_col[i] = 0
                v_dia1[depth-i+N] = 0
                v_dia2[depth+i] = 0
        

        


if N % 2 == 0:
    solution(0, True)
    print(cnt*2)
else:
    solution(0, False)
    print(cnt)