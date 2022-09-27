N = int(input())
A = list(map(int, input().split(' ')))
visited = [0 for _ in range(N)]

result = 0
def solution(depth, total, preIdx):
    global result

    if depth == N-1:
        result = max(result, total)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, total+abs(A[preIdx]-A[i]), i)
            visited[i] = 0

# for문을 하는 이유는 
# depth가 0인 경우를 solution 밖에서 한 것임
    # depth가 0이이면 preIdx를 지정할 수 없으니까 
for i in range(N):
    visited[i] = 1
    # total과는 +를 할 뿐 -> 0으로 시작해야 함
    solution(0, 0, i)
    visited[i] = 0

print(result)