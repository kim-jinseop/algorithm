
from re import M
from unittest import result


n,m = map(int,input().split())
result = 0

for i in range(n) :
    data = list(map(int,input().split()))

    Min = min(data) 

    result = max(result,Min)

print(result)    