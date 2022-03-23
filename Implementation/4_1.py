# 상하좌우

N = int(input())
move_list = input().split()

x, y = 1, 1
drection = ['L', 'R', 'U', 'D']
ax = [0,0,-1,1]
ay = [-1,1,0,0]


for move in move_list :
    for i in range(len(drection)) :
        if move==drection[i] :
            sx = x + ax[i]
            sy = y + ay[i]
            
    if sx<1 or sx>N or sy<1 or sy>N :
        continue
    else :
        x = sx
        y = sy   
        
print(x,y)