import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    grade = list(map(int, input().split(' ')))
    num = grade[0]
    total = sum(grade[1:], start = 0)
    avg = total / num
    upper = [val for val in grade[1:] if val > avg]
    print('{:.3f}%'.format(len(upper)/num * 100))
