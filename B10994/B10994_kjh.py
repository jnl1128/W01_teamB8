n = int(input())

def draw_star(n):
    if n == 1:
        return ['*']
    sub_star = draw_star(n-1)
    new_star = []
    new_star.append('*'*(4*n-3))
    new_star.append('*' + ' ' * (4*n-5) + '*')
    for i in sub_star:
        new_star.append('* ' + i + ' *')
    new_star.append('*' + ' ' * (4*n-5) + '*')
    new_star.append('*'*(4*n-3))
    return new_star

star = draw_star(n)
for i in star:
    print(i)