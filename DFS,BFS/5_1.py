#DFS

# input
n, m = map(int,input().split())

grape = []
for i in range(n) :
    grape.append(list(map(int,input().split())))
    
# dfs func
def dfs(x,y) :
    # 음수나 초과하는 값이 재귀되면 False 로 return 
    if x < 0 or x >= n or y < 0 or y >= m : 
        return False
    
    # 방문처리 및 인접노드 DFS(재귀)
    if grape[x][y] == 0 :
        grape[x][y] = 1
        
        dfs(x,y-1) #좌
        dfs(x,y+1) #우
        dfs(x-1,y) #상
        dfs(x+1,y) #하
        
        return True
    
    # 방문된곳이면 False로 return
    else : 
        return False
    
# dfs run
result = 0    
for i in range(n) :
    for j in range(m) :    
        if dfs(i,j) == True :
            result += 1
            
print(result)