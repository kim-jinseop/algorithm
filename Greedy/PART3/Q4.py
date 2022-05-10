# 만들 수 없는 금액
n = int(input())
array = list(map(int,input().split()))
array.sort()

target = 1
for i in array :
    if target < i :
        break
    else :
        target += i
    
print(target)    