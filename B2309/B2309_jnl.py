heights = []

for _ in range(9):
    heights.append(int(input()))

result = []
cur = []

def splice(arr, k):
    return arr[0:k]+arr[k+1:len(arr)]

done = False
def findHobit(arr, n):
    global done

    if not done:
        global result

        if n == 0:
            if sum(cur) == 100:
                cur.sort()
                for i in (cur):
                    print(i)
                done = True

        for i in range(len(arr)):
            cur.append(arr[i])
            findHobit(splice(arr, i), n-1)
            cur.pop()
    
findHobit(heights, 7)
