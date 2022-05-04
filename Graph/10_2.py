# plan to devide the sity

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a<b :
        parent[b] = a
    else :
        parent[a] = b
        
n, m = map(int,input().split()) #집의 개수, 길의 개수

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

array = []
for _ in range(m):
    a,b,cost = map(int,input().split())
    array.append((cost,a,b))
array.sort()

result = 0    
for edge in array:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union(parent, a, b)
        result += cost
        last = cost
        
print(result-last)    