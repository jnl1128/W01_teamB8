import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
used = [0]*n
def solution(depth, pre, result):
    if depth == m:
        sys.stdout.write(result+'\n')
        return
    for i in range(pre, n):
        if used[i] == 0:
            used[i] = 1
            solution(depth+1, i+1, result + str(nums[i]) + " ")
            used[i] = 0
    
solution(0, 0, '')