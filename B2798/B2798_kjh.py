n, m = map(int, input().split())
card_list = sorted(list(map(int, input().split())))
used = [0 for _ in range(n)]

answer = 0
sum = 0

for i in range(len(card_list)):
    sum = card_list[i]
    s = 0
    e = len(card_list)-1
    while s < e:
        if s == i:
            s += 1
            continue
        elif e == i:
            e -= 1
            continue

        if sum + card_list[s] + card_list[e] > m:
            e -= 1
        else:
            answer = max(answer, sum + card_list[s] + card_list[e])
            s += 1

print(answer)