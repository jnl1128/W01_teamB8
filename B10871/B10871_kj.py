n, x = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    print(f'{num} ' if x>num else '', end="")