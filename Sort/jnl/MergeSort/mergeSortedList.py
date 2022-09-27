# 이미 정렬된 배열의 병합
from typing import Sequence, MutableSequence

# a = [1,9,10, 11] # b = [2,6,20]
# c = [None, None, None, None, None, None, None]
def merge_sorted_list(a: Sequence, b: Sequence, c:MutableSequence) -> None:
    # 각 배열의 커서
    pa, pb, pc = 0, 0, 0
    na, nb = len(a), len(b)

    # a, b모두 아직 끝나지 않은 상태
    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    # c = [1, 2, 6, 9, 10, 11] -> #a만 끝남

    # b만 끝난 상태
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1

    # a만 끝난 상태
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1
    # c = [1, 2, 6, 9, 10, 11, 20]

if __name__ == '__main__': 
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None]*(len(a) + len(b))

    merge_sorted_list(a, b, c)

    print('배열 a: {}\n'.format(a))
    print('배열 b: {}\n'.format(b))
    print('배열 c: {}'.format(c))
