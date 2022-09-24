import sys

n = int(sys.stdin.readline().rstrip())
words = list()
for _ in range(n):
    words.append(sys.stdin.readline().rstrip())
print(*sorted(list(set(words)), key=lambda x: (len(x), x)), sep="\n")