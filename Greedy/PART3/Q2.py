# 곱하기 혹은 더하기
n = input()

list = []
for i in n:
    list.append(int(i))
    
result = 0    
for i in list :
    if i <= 1 or result <= 1:
        result = result + i
    else :
        result = result * i

print(result)