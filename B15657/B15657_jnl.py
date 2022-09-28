#N과 M(8)
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

def solution(depth, stack, start):
    if depth == M:
        print(*stack,sep=' ')
        return
    
    for i in range(start,N):
        solution(depth+1, stack+[arr[i]], i)
    
solution(0, [], 0)
