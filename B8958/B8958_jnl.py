import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    quiz = list(input())
    result = 0  
    cnt = 0
    for val in quiz:
        if val == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    
    print(result)