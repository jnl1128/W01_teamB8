heights = list(map(int, open(0).read().split()))

flag = True
answer = list()
used = [0 for _ in range(9)]

def solution(depth, result):
    global answer
    global flag

    if flag is False:
        return 
    
    if depth == 2:
        h_sub_r = [x for x in heights if x not in result]
        if sum(h_sub_r) == 100:
            flag = False
            answer = h_sub_r.copy()
        return

    for i in range(len(heights)):
        if used[i] == 0:
            used[i] = 1
            solution(depth+1, result + [heights[i]])
            used[i] = 0
            

solution(0, [])
print(*sorted(answer), sep="\n")
