# https://www.acmicpc.net/problem/15686

from itertools import combinations

n,m = map(int,input().split())

house = []
chicken = []

def serch_sum(candidate) :
    result = 0
    for hx, hy in house :
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))

        result += temp
    return result

for r in range(n) :
    array = list(map(int,input().split()))
    for c in range(n) :
        if array[c] == 1 :
            house.append((r,c))
        elif array[c] == 2 :
            chicken.append((r,c))

candidates = list(combinations(chicken, m))

result = 1e9
for candidate in candidates :
    result = min(result, serch_sum(candidate))

print(result)
