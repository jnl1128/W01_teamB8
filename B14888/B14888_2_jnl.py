# 연산자 끼워넣기
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))
O = list(map(int, input().split(' ')))

min_result = 1000000000
max_result = -1000000000

def solution(depth,total):
    global min_result, max_result

    if depth == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    for i in range(4):
        if O[i] > 0:
            O[i] -= 1
            nextTotal = 0
            if i == 0:
                nextTotal = total + A[depth]
            elif i == 1:
                nextTotal = total -  A[depth]
            elif i == 2:
                nextTotal = total * A[depth]
            else:
                if total < 0:
                    nextTotal = -((-total)//A[depth])
                else:
                    nextTotal = total // A[depth]
            solution(depth+1, nextTotal)
            O[i] += 1

solution(1, A[0]) 
sys.stdout.write('{}\n{}'.format(max_result, min_result))
            
        
    
   