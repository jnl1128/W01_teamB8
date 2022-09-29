n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]
used = [0] * (n)

total = sum(sum(t) for t in team)
min_gap = sum(sum(t) for t in team) + 1

def solution(depth, k, team_link, pre_index):
    global min_gap
    if depth == k:
        link_score = get_team_ability(team_link)
        team_start = [x for x in [i for i in range(n)] if x not in team_link]
        start_score = get_team_ability(team_start)
        min_gap = min(min_gap, abs(link_score-start_score))
        return
    for i in range(pre_index, n):
        if used[i] == 0:
            used[i] = 1
            solution(depth+1, k, team_link + [i], i+1)
            used[i] = 0


def get_team_ability(target_team):
    ablty_sum = 0
    for i in range(len(target_team)):
        for j in range(len(target_team)):
            ablty_sum += team[target_team[i]][target_team[j]]
    return ablty_sum


solution(0, n//2, [], 0)

print(f'{min_gap}')
