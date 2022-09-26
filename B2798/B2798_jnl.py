#블랙잭 #반복
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))
cards.sort()

result = 0

for i in range(len(cards)-2):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if (cards[i]+cards[j]+cards[k]) <= M:
                result = max(result,cards[i]+cards[j]+cards[k])
print(result)
