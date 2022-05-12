# 문자열 재정렬 

n = input()

list = []
sum = 0

for i in range(len(n)) :
    if n[i].isalpha() :
        list.append(n[i])
    else :
        sum += int(n[i])
        
list.sort()

if sum != 0 :
    list.append(str(sum))
    
print(''.join(list))            