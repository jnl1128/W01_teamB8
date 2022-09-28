# 로또
def solution(depth, stack, start):
    if depth == 6:
        result.append(stack)
        # # stack.sort()
        # if stack not in result:
        #     result.append(stack)
        return
    
    for i in range(start,K):
        if visited[i] == 0:
            visited[i] = 1
            solution(depth+1, stack+[lotto[i]], i)
            visited[i] = 0

string = input()
while int(string[0]) != 0:
    arr = list(map(int, string.split(' ')))
    K= int(arr[0])
    lotto = arr[1:]

    visited = [0 for _ in range(K)]
    lotto.sort()
    result = []

    solution(0, [], 0)

    for elem in result:
        print(*elem, sep=' ')
    print('')
    
    string = input()
