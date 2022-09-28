n, m = map(int, input().split())

used = [0] * (n+1)

def solution(depth, result):
    if depth == m:
        print(result)
        return
    for i in range(1, n+1):
        if used[i] == 0:
            used[i] = 1
            solution(depth+1, result + str(i)+ ' ')
            used[i] = 0

solution(0, '')