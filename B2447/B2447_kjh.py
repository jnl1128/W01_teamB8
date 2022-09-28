N = int(input())

def solution(n):
    if n == 1:
        return ['*']
    
    sub_star = solution(n//3)
    new_star = []
    for star in sub_star:
        new_star.append(star * 3)
    for star in sub_star:
        new_star.append(star + ' '*(n//3) +star)
    for star in sub_star:
        new_star.append(star * 3)

    return new_star

star = solution(N)
for i in star:
    print(i)
