a = int(input())
b = int(input())

print(f'{b%10 * a}')
print(f'{b//10%10 * a}')
print(f'{b//100%10 * a}')
print(f'{a*b}')