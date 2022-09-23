a, b, v = map(int, input().split())
day = (v-a)//(a-b)
print([day+1, day+2][(v-a)%(a-b) > 0])