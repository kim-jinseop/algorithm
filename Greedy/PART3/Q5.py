# Greedy - 볼링공 고르기 

''' input data

8 5
1 5 4 3 2 4 5 2

'''

n, m = map(int,input().split()) # 볼링공의 개수 n / 공의 최대 무게 m 
array = list(map(int,input().split()))

count = 0
for i in range(n) :
    for j in range(i,n) :
        if array[i] != array[j] :
            count += 1 

print(count)