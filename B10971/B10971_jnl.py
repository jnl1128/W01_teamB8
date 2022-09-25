import sys

N = int(input())
min_value = 1000000* (N)
travel = []
for _ in range(N):
    travel.append(list(map(int,input().split(' '))))

def dfs(startNode, nextNode, value, visited):
    global min_value
    # 모두 순회하지 않아도 min_value를 초과하면 dfs함수 끝내기
    if value + travel[nextNode][startNode] > min_value:
        return 

    if len(visited) == N:
        if travel[nextNode][startNode] != 0:
            # min_value 최신화
            min_value = value + travel[nextNode][startNode]
            return
        return 

    for i in range(N):
        # 갈 수 있는 곳인지 
        # 제자리걸음이 아닌지
        # 이미 방문했던 노드는 아닌지 
        # startNode가 계속 그대로인 이유: 마지막으로 돌아올 노드가 무엇인지 명시하기 위해서
        if travel[nextNode][i] != 0 and i != startNode and i not in visited:
            visited.append(i)
            # i는 이동한 노드
            # 0에서 제일 처음 시작했고, 현재 위치가 1이고 visited가 [0, 1]이라면
            # 위의 if문에서 처음으로 통과한 i는 2일 것
            dfs(startNode, i, value+travel[nextNode][i], visited)
            visited.pop()

# i는 시작하는 node
# [i]를 하는 이유는 시작점 == 처음부터 방문한 곳
# 기본적으로 backtracking
result = 0
for i in range(N):
    # N번 for문을 도는 이유는 출발지를 선태할 수 있는 방법이 N개이기 때문
    dfs(i, i, 0, [i])
        

print(min_value)