N, r, c = map(int, input().split())

def get_num(min, N, r, c):
    if N == 0:
        print(min)
        return
    # print(f'row check :: {r} < {2 ** (N-1)} == {r < 2 ** (N-1)}')
    if r < 2 ** (N-1):
        # print(f'col check :: {c} < {2 ** (N-1)} == {c < 2 ** (N-1)}')
        if c < 2 ** (N-1):
            # print(f'case1:: {min} 이상 {min + (2 ** (N-1)) * (2 ** (N-1)) -1} 이하')
            # print(f'----> get_num({min}, {N-1}, {r}, {c})')
            get_num(min, N-1, r, c)
        else:
            c -= 2 ** (N-1)
            # print(f'case2:: {min + (2 ** (N-1)) * (2 ** (N-1))} 이상 {min + (2 ** (N-1)) * (2 ** (N)) -1} 이하')
            # print(f'----> get_num({min + (2 ** (N-1)) ** 2}, {N-1}, {r}, {c})')
            get_num(min + (2 ** (N-1)) ** 2, N-1, r, c)
    else:
        r -= 2 ** (N-1)
        # print(f'col check :: {c} < {2 ** (N-1)} == {c < 2 ** (N-1)}')
        if c < 2 ** (N-1):
            # print(f'case3:: {min + (2 ** (N-1)) * (2 ** (N))} 이상 {mid -1} 이하')
            # print(f'----> get_num({min + (2 ** (N-1)) * (2 ** (N))}, {N-1}, {r}, {c})')
            get_num(min + (2 ** (N-1)) * (2 ** (N)), N-1, r, c)
        else:
            c -= 2 ** (N-1)
            # print(f'case4:: {mid} 이상 {min + (2 ** (N)) * (2 ** (N)) -1} 이하')
            # print(f'----> get_num({mid}, {N-1}, {r}, {c})')
            get_num(min + (2 ** (N-1)) ** 2 + (2 ** (N-1)) * (2 ** (N)), N-1, r, c)


get_num(0, N, r, c)