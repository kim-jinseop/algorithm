# https://www.acmicpc.net/problem/15686

from itertools import combinations

n,m = map(int,input().split())

house = []
chicken = []

for r in range(n) :
    array = list(map(int,input().split()))
    for c in range(n) :
        if array[c] == 1 :
            house.append((r,c))
        elif array[c] == 2 :
            chicken.append((r.c))

combi = list(combinations(chicken, m))

