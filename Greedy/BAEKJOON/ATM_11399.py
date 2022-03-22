N = int(input())
P = list(map(int,input().split()))

SP = P.sort()

result = 0
sum = 0

while N!=0 :
    for i in range(N) :
        sum = sum + P[i]
    
    result += sum
    
    N -= 1
    sum = 0
    
print(result)