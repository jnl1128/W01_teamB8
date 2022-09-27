import sys


def lotto(depth, result, used, last):
    if depth == 6:
        for r in result:
            sys.stdout.write(f'{r} ')
        sys.stdout.write('\n')
        return

    for i in range(last, len(s)):
        if used[i] == 0:
            used[i] = 1
            lotto(depth+1, result + [s[i]], used, i+1)
            used[i] = 0
    

s = sys.stdin.readline()
while int(s[0]) != 0:
    s = list(map(int, s.split()))[1:]
    lotto(0, [], [0] * len(s), 0)
    sys.stdout.write('\n')
    s = sys.stdin.readline()
