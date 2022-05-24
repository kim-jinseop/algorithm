# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

result = []
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def solution(n, build_frame):

    # map data 기둥, 보 유무 
    # 1은 기둥이 설치된 곳으로 기둥과 보를 설치할 수 있는 위치
    # 2는 보가 설치된 곳으로 기둥은 설치 할 수 있으며, 보는 y+2 가 '2' 일때 설치 가능
    data = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1) :
        data[0][i] = 1 # 바닥은 1 로 초기화 

    for frame in build_frame :
        x,y = frame[0] , frame[1] # 가로, 세로
        a = frame[2] # 0: 기둥 or 1: 보
        b = frame[3] # 0: 삭제 or 1: 설치

        if b==1 :
            create(data,x,y,a)
        elif b==0 :
            remove(data,x,y,a)

    return result

def create(data,x,y,a):
    if a==0:
        if data[y][x] == 1 or data[y][x] == 2 : 
            data[y+1][x] = 1
            result.append([x,y,a])
            
    elif a==1 :
        if data[y][x] == 1 :
            data[y][x+1] = 2
            result.append([x,y,a])
            
        elif data[y][x+1] == 1 : 
            data[y][x] = 2
            result.append([x,y,a])
            
        elif data[y][x]==2 and data[y][x+1]==2 :
            result.append([x,y,a])    
            
    return

def remove(data,x,y,a):
    # if a==0 :
    #     if data[y+1][x] != 1 and (data[y+1][x-1] == 2 and data[y+1][x-1] == 2) :
    #         result.remove([x,y,a])          
    # elif a==1 :
        
    # return

print(solution(n, build_frame))
