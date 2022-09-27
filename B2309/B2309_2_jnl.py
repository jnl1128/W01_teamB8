# 일곱 난쟁이
import sys
input = sys.stdin.readline
# 입력받기
heights = []
for _ in range(9):
    heights.append(int(input()))
heights.sort()
sum9 = sum(heights)
visited = [0 for _ in range(9)] 

flag = True

def solution(depth, total):
    global flag
    if flag:
        if depth == 2:
            if total == sum9 - 100:
                flag = False
                for idx, height in enumerate(heights):
                    if visited[idx] == 0:
                        sys.stdout.write('{}\n'.format(height))
            return
        
        for i in range(9):
            if visited[i] == 0:
                visited[i] = 1
                solution(depth+1, total+heights[i])
                visited[i] = 0

solution(0, 0)





