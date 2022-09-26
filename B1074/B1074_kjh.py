N, r, c = map(int, input().split())

def get_num(min, N, r, c):
    if N == 0:
        print(min)
        return

    if r < 2 ** (N-1):
        if c < 2 ** (N-1):
            get_num(min, N-1, r, c)
        else:
            c -= 2 ** (N-1)
            get_num(min + (2 ** (N-1)) ** 2, N-1, r, c)
    else:
        r -= 2 ** (N-1)
        mid = ((min + (2 ** (N-1)) * (2 ** (N)) ) + (min + (2 ** (N)) * (2 ** (N)) -1))//2 + 1
        if c < 2 ** (N-1):
            get_num(min + (2 ** (N-1)) * (2 ** (N)), N-1, r, c)
        else:
            c -= 2 ** (N-1)
            get_num(mid, N-1, r, c)
    

get_num(0, N, r, c)