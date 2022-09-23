a = int(input())
c = int(input())

b = c
print(a* (b%10))
b = b - b%(10)
print(a*((b//10)%10))
b = b - b%(100)
print(a*((b//100)))
print(a*c)

##1