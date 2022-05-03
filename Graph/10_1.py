# create team 

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b :
        parent[b] = a
    else :
        parent[a] = b
        
v, e = map(int,input().split())

parent = [0] * (v+1)
for i in range(1,v+1) :
    parent[i] = i
    
for _ in range(e) :
    x,a,b = map(int,input().split())    
    
    if x==0 :
        union(parent,a,b)
    elif x==1:
        if find_parent(parent,a) != find_parent(parent,b) :
            print('NO')
        else :
            print('YES')