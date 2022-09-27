a = [1, 2]
def changeList(arr):
    arr[0], arr[1] = arr[1], arr[0]
    return
# print(a)
# changeList(a)
# print(a) 
#함수의 인자로 받은 리스트의 원소 자체가 바뀐다 #얕은 복사
aa = [1, 2]
def changedByFunction(arr):
    arr[0] = 5
    print(arr)
    changeList(arr)
    return arr

print(aa)
#1
print(changedByFunction(aa))
#2
print(aa)
#1과 2는 같은 결과 출력 <- 결국 같은 주소에 가서 값만을 바꿔주니까


b = 1
def changeInteger(num):
    num = 2
    num *= 2
    return
print(b)
changeInteger(b)
print(b) #함수의 인자로 받은 정수는 그 값이 바뀌게 되면 새로운 정수 객체를 만든다. #인자로 받은 b 자체가 바뀌지 않는다.
