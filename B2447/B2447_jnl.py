# 별 찍기 #메모리 초과남...
import sys, math
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
k = int(N ** (1.0/3.0))
visited = [0 for _ in range(k)]

def solution(depth, string):
    if depth == k:
        print(string)
        return

    nextString = ''
    arr = string.split('\n')
    for i in range(3):
        for elem in arr:
            if not elem:
                continue
            if i % 3 == 1:
                nextString += elem+' '* 3**(depth)+elem
            else:
                nextString += elem * (3)
            nextString += '\n'  
    solution(depth+1, nextString)
        

solution(1, '***\n* *\n***')