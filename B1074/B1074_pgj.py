import sys
sys.setrecursionlimit(10**7)

cnt = 0
def find_num(N, r, c):
    global cnt
    if(N == 1):
        return
    if(r < N//2 and c < N//2):
    #좌표가 1사분면일 때
        find_num(N//2, r, c)
    elif(r < N//2 and c >= N//2):
    #좌표가 2사분면일 때
        cnt += N * N // 4
        find_num(N//2, r, c - N//2)
    elif(r >= N//2 and c < N//2):
    #좌표가 3사분면일 때
        cnt += (N * N // 4) * 2
        find_num(N//2, r-N//2, c)
    else:
    #좌표가 4사분면일 때
        cnt += (N * N // 4) * 3
        find_num(N//2, r - N//2, c - N//2)




N, r, c = map(int, input().split())
size = 2 ** N
find_num(size, r, c)
print(int(cnt))