import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

def solution(depth, result):
    if depth == m:
        sys.stdout.write(result+"\n")
        return
    for i in range(n):
        solution(depth+1, result + str(nums[i])+ ' ')

solution(0, '')