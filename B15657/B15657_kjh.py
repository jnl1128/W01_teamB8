import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

def solution(depth, pre, result):
    if depth == m:
        sys.stdout.write(result+"\n")
        return
    for i in range(pre, n):
        solution(depth+1, i, result + str(nums[i])+ ' ')

solution(0, 0, '')