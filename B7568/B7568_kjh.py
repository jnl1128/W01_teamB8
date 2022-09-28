n = int(input())
people = [[0]*3 for _ in range(n)]
for i in range(n):
    people[i] = list(map(int, input().split())) + [0]

for i in range(n):
    rank = 1
    p = people[i]
    for j in range(n):
        if p[0] < people[j][0] and p[1] < people[j][1]:
            rank += 1
    p[2] = rank

for i in range(len(people)):
    print(people[i][2], end=" ")