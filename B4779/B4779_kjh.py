def solution(N, bar, s, e):
    if N == 0:
        return
    for i in range(s+(e-s)//3, s+((e-s)*2)//3):
        bar[i] = ' '
        
    solution(N-1, bar, s, (s+(e-s)//3))
    solution(N-1, bar, s+((e-s)*2)//3, e)
    return 0


while True:
    try:
        n = int(input())
        bar = ['-']*(3**n)
        solution(n, bar, 0, int(3**n))
        print(*bar, sep="")
    except EOFError:
        break