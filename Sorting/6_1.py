# up and down

count = int(input())

array = []
for _ in range(count) :
    array.append(int(input()))
    
array.sort(reverse=True)

for i in array :
    print(i,end=' ')