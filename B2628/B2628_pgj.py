a,b = map(int, input().split())
count = int(input())

arr_a = [0]
arr_b = [0]

cut_a = []
cut_b = []
for i in range(count):
    m, c = map(int, input().split())
    if(m == 0):
        arr_b.append(c)
    else:
        arr_a.append(c)
arr_a.append(a)
arr_b.append(b)
arr_a.sort()
arr_b.sort()

cut_size_a = 0
cut_size_b = 0
for i in range(1,len(arr_a)):
    cut_a.append(arr_a[i]-arr_a[i-1])
for i in range(1,len(arr_b)):
    cut_b.append(arr_b[i]-arr_b[i-1])

    
print(max(cut_a)*max(cut_b))
# for i in range(len(cut_a)):
#     for j in range(len(cut_b)):
#         if(max < cut_a[i]*cut_b[j]):
#             max = cut_a[i]*cut_b[j]

# print(max)