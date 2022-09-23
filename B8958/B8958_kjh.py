testcase = int(input())
for test in range(testcase):
    print(sum((len(i)*(len(i)+1))//2 for i in input().split('X')))