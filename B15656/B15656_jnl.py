#N과M(7)
import sys
input = sys.stdin.readline
N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

def solution(depth, stack):
    if depth == M:
        print(*stack, sep=' ')
        return

    for i in range(N):
        solution(depth+1, stack+[arr[i]])
            

solution(0, []) 