w, h = map(int, input().split())
x_points = [0]
y_points = [0]
for _ in range(int(input())):
    c = list(map(int, input().split()))
    [y_points, x_points][c[0]].append(c[1])
y_points.append(h)
x_points.append(w)
list.sort(x_points)
list.sort(y_points)

ans = 0
for i in range(len(x_points)-1):
    width = x_points[i+1] - x_points[i]
    for j in range(len(y_points)-1):
        height = y_points[j+1] - y_points[j]
        ans = max(ans, width*height)
print(ans)
