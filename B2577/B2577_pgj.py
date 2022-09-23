a = int(input())
b = int(input())
c = int(input())

abc = a * b * c

str_abc = str(abc)

for i in range(10):
    count = 0
    for j in range(len(str_abc)):
        if(int(str_abc[j]) == i):
            count += 1
    print(count)