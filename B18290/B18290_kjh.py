import sys
n, m, k = map(int, sys.stdin.readline().split())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [0] * (n*m)

max_num = -9876543210000

def solution(depth, result, pre):
    global max_num

    if depth == k:
        max_num = max(max_num, result)
        return

    # 문제 조건에 따라 각 칸이 가질 수 있는 최대값은 10000 이다.
    # 따라서 남은 갯수(k-depth) 의 칸이 모두 10000 이라도
    # max_num 보다 작다면, 이후의 계산은 의미가 없으므로
    # 탐색을 종료한다.
    if result + 10000 * (k-depth) < max_num:
        return
    
    for i in range(pre, m * n):
        if visited[i] == 0:
            row = i // m
            col = i % m
            flag = True
            for x, y in move:
                if 0 <= (x+row) < n and 0 <= (y+col) < m:
                    if visited[(x+row)*m+y+col] == 1:
                        flag = False
                        break
            if flag is True:
                visited[i] = 1
                solution(depth+1, result+nums[row][col], i+1)
                visited[i] = 0


solution(0, 0, 0)
sys.stdout.write(f'{max_num}')