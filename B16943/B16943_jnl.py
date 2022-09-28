# 숫자 재배치
import sys
input = sys.stdin.readline

A, B = map(int, input().split(' '))
nA = len(str(A))
arr = []
for char in str(A):
    arr.append(char) #[1 2 3 4]

visited = [0 for _ in range(nA)]

result = 0
def solution(depth, stack):
    global result, nA, arr
    # nA = 4
    if depth == nA:
        total = int(''.join(stack))
        if result < total and total < B:
            result = total
        return
    
    for i in range(nA):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, stack+[arr[i]])
            visited[i] = 0

solution(0, [])

if result < B :
    print(-1)
else:
    print(result)

