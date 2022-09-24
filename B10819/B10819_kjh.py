import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
used = [0 for _ in range(n)]

ans = 0
def solution(depth, pre, sum):
    global ans
    global used

    if depth == n-1:
        ans = max(ans, sum)
        return
    for i in range(len(num_list)):
        if used[i] == 0:
            used[i] = 1
            solution(depth+1, i, sum + abs(num_list[i] - num_list[pre]))
            used[i] = 0

for i in range(len(num_list)):
    used[i] = 1
    solution(0, i, 0)
    used[i] = 0

sys.stdout.write(f'{ans}')