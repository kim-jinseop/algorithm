#서로소 집합을 이용한 cycle 판별

#-----------------------------------------------------------
# 특정 원소가 속한 집합 찾기    
def find_parent(parent, x) :   
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]    #압축

# 두 원소가 속한 집합을 합치기
def union(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a<b :
        parent[b] = a
    else :
        parent[a] = b
#-----------------------------------------------------------        
v, e = map(int,input().split()) #노드,간선 입력 
parent = [0] * (v+1) #부모테이블 생성 및 0을 초기화

# 부모 테이블 상에서 자기 자신의 값으로 초기화 
for i in range(1,v+1) :
    parent[i] = i
    
cycle = False

for i in range(e) :
    a, b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b) :
        cycle = True
        break
    else :
        union(parent,a,b)
        
if cycle:
    print("사이클이 발생했습니다.")
else :
    print("사이클이 발생하지 않았습니다.")    