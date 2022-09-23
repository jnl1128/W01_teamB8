testcase = int(input())
for test in range(testcase):
    sum = 0
    score = 0
    for r in input():
        if r == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)