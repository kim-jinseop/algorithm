#cycle check 

from gettext import find


def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b :
        parent[b] = a
    else :
        parent[a] = b 

# 노드의 개수와 간선의 개수 받기
v, e = map(int,input().split())
parent = [0] * (v+1)

# 부모테이블 자기자신으로 초기화
for i in range(1,v+1) :
    parent[i] = i

edges = [] # 간선을 담을 리스트
result = 0 # 총합

# 모든 간선의 정보 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 간선을 비용순으로 정리
edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent,a) != find_parent(parent,b) :
        union(parent, a, b)
        result += cost

print(result)