from re import S
import sys


def colorpaper(n, x, y):
    global blue, white
    if n == 1:
        if(arr[x][y] == 1):
            blue += 1
        else:
            white +=1
        return
    color = check_color(n, x, y)
    if color != -1:
        if(color == 1):
            blue+=1
        else:
            white+=1
        return

    size = n // 2
    colorpaper(size, x, y)
    colorpaper(size, x, y+size)
    colorpaper(size, x+size, y)
    colorpaper(size, x+size, y+size)

def check_color(size, x, y):
    color = arr[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != arr[i][j]:
                return -1
    return color

n = int(sys.stdin.readline().rstrip())
arr = [0] * n
white = 0
blue = 0
for i in range(n):
    arr[i] = (list(map(int,sys.stdin.readline().strip().split())))

print(arr)    

colorpaper(n, 0, 0)


print(white)
print(blue)