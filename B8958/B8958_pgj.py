a = int(input())
arr = []

for i in range(a):
    input_item = input()
    arr.append(str(input_item))

for i in range(a):
    score = 0
    count = 0
    for j in range(len(arr[i])):
        
        if(arr[i][j] == 'O'):
            count = count+1
            score = score + count
        elif(arr[i][j] == 'X'):
            count = 0
    print(score)   