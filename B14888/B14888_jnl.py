import sys, copy
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split(' ')))
A = A[::-1]
O = list(map(int,input().split(' ')))
O_arr = []
for i in range(4):
    O_arr += [str(i)]*O[i]
    
string = []
result_s = set()


def splice(arr, n): # 본인은 제외한 것을 리턴해주는 함수
    return arr[0:n] + arr[n+1:len(arr)] # arr은 안 건드리고 본인은 제외한 리스트를 새로 만들어서 리턴해주는 것

def makePermutation(arr, k):
    global string
    n = len(arr)  
    
    if k <= 0 :
        result_s.add(''.join(string))
        return   

    for i in range(n):  
        string.append(arr[i])
        makePermutation(splice(arr,i), k-1) # 방금 전에 뽑은 것을 리스트에서 제외하고 그 중에서 k-1개 뽑아줘야 함
        string.pop() # string을 pop해줘야 복구가 됨

makePermutation(O_arr, N-1)

result = []
def operate(arr, strOperator):
    global result
    arrOperator = list(strOperator)
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        operator = arrOperator.pop()
        if operator == '0':
            arr.append(a+b)
        elif operator == '1':
            arr.append(a-b)
        elif operator == '2':
            arr.append(a*b)
        else:
            if a < 0:
                arr.append(-((-a)//b))
            else:
                arr.append(a//b)
    result.append(arr[0])
 
for s in result_s:
    a = copy.deepcopy(A)
    operate(a, s)

sys.stdout.write('{}\n{}'.format(max(result), min(result)))
# print(max(result), min(result),)