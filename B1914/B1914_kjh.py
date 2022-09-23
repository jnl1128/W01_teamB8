n = int(input())

path_list = []

def hanoi(start, mid, dest, depth):
    if depth == n:
        return
    hanoi(start, dest, mid, depth+1)
    global path_list
    path_list.append(f'{start} {dest}')
    hanoi(mid, start, dest, depth+1)

print(2**n -1)
if n <= 20:
    hanoi(1, 2, 3, 0)
    print(*path_list, sep='\n')
    
'''
3 -> 7
4 -> 15
5 -> 31
6 -> 63
'''