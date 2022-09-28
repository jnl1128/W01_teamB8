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