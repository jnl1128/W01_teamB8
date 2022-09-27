# 별 찍기 #내가 안짠 #아니 #내가 못짠 #남이 잘짠 #정답코드
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
k = int(N ** (1.0/3.0))

def solution(depth):
    if depth == 1:
        # print(string)
        return ['*']

    arr = solution(depth//3)
    lst = []
    
    for elem in arr:
        lst.append(elem*3)
    for elem in arr:
        lst.append(elem+' '*(depth//3)+elem)
    for elem in arr:
        lst.append(elem*3)

    return lst

print('\n'.join(solution(N)))
