
def check_queen(x):
    for i in range(x):
        if(row[x] == row[i] or abs(row[x] - row[i]) == x - i): #같은 행에 있거나, 대각선에 있는 경우
            return False
    return True
    

def dfs(y):
    global result

    if(y == N):
        result += 1
        print(row)
    else:
        for i in range(N):
            row[y] = i
            if(check_queen(y)): # 퀸을 체크했을 때  True가 반환되면
                dfs(y+1) # 한 층 더 내려감
N = int(input())
row = [0] * N
result  = 0
dfs(0)
print(result)
# N의 갯수만큼 추가
# 인덱스 : y축, 내부 값 : x축