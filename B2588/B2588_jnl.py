import sys
input = sys.stdin.readline 

A = int(input())
B = int(input())

B100 = B//100
B -= B100*100
B10 = B//10
B -= B10*10
B1 = B

num3 = A * B1
num4 = A * B10 
num5 = A * B100
num6 = num3 + num4*10 + num5*100

print(num3, num4, num5, num6, sep="\n")
