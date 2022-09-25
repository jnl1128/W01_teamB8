import sys
input = sys.stdin.readline

N = int(input())


def checkDiagonal(row, col,visited):

    for i in range(1, N):
        if row+(-1*i) >= 0 and  0<=col+(1*i)<N:
            if visited[row+(-1*i)] == col+(1*i):
                return False
        if row+(-1*i) >= 0 and 0<=col+(-1*i)<N :
            if visited[row+(-1*i)] ==col+(-1*i):
                return False
    return True

    
    
    

cnt = 0
def dfs(visited):
    global cnt 
    if len(visited) == N:
        cnt += 1
        return 

    for i in range(N):
        # 갈 수 있는 곳인지 
        # 대각선 검증 # col 검증 # row 검증은 할 필요 없음
        if i not in visited and checkDiagonal(len(visited), i, visited):
            visited.append(i)
            dfs(visited)
            visited.pop()
            
                
    

# i : 0번째 row의 i col에 퀸을 둘 것인지
# 기본적으로 backtracking
for i in range(N):
    dfs([i])
    
sys.stdout.write('{}'.format(cnt))