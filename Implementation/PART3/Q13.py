# https://www.acmicpc.net/problem/15686

from itertools import combinations

n,m = map(int,input().split())

house = []
chicken = []

def serch_sum(candidate) :
    result = 0
    for hx, hy in house :
        temp = 1e9 # 1e9 : 무한과 유사한 값
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy)) # abs : 절대값

        result += temp
    return result

for r in range(n) :
    array = list(map(int,input().split()))
    for c in range(n) :
        if array[c] == 1 :
            house.append((r,c))
        elif array[c] == 2 :
            chicken.append((r,c))

candidates = list(combinations(chicken, m)) # combiations : 경우의 수를 뽑아낸다(조합)

result = 1e9
for candidate in candidates :
    result = min(result, serch_sum(candidate))

print(result)
