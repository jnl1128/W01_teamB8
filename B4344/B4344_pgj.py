a = int(input())

inputt = []
for i in range(a):
    sum = 0
    count = 0
    inputt = input().split()
    inputt = list(map(int, inputt))
    for j in range(1, len(inputt)):
        sum = sum + inputt[j]

    average = sum / inputt[0]
    for j in range(1, len(inputt)):
        if(inputt[j] > average):
            count = count + 1

    percentage = count / inputt[0] * 100
    print('{:.3f}'.format(percentage)+"%")