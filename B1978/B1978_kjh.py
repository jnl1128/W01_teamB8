def is_prime_num(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i+=1
    return True

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(sum(1 for num in nums if is_prime_num(num)))
    

if __name__ == '__main__':
    main()
