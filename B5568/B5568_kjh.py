n = int(input())
k = int(input())
card_list = []
for _ in range(n):
    card_list.append(input())

used = [False for _ in range(n)]
ans = set()

def solution(depth, result):
    if depth == k:
        ans.add(result)
        return
    for i in range(n):
        if used[i] is False:
            used[i] = True
            solution(depth+1, result+card_list[i])
            used[i] = False

solution(0, "")
print(len(ans))