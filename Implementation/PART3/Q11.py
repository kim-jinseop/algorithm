# https://www.acmicpc.net/problem/3190

n = int(input()) #보드의 크기 N*N
k = int(input()) #사과의 개수

map_data = [[0] * (n+1) for _ in range(n+1)]
apple_array = [[0] * (n+1) for _ in range(n+1)] 

for _ in range(k) :
    a, b = map(int,input().split())
    apple_array[a][b] = 1

# 방향 관련
l = int(input()) #방향전환 횟수
info = []
for _ in range(l) :
    x,c = input().split()
    info.append((int(x),c))

# 좌상우하 
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def Rotation(way,direction) :
    if way == 'D' : #오른쪽 회전
        direction = (direction + 1) % 4
    elif way == 'L' :
        direction = (direction - 1) % 4
    return direction

def program() :
    # 초기상태 - 내위치,방향 
    x,y = 1,1
    map_data[y][x] = 1
    direction = 2
    time = 0
    index = 0
    q = [(y,x)]

    while True :
        my = y + dy[direction] #이동 후 좌표
        mx = x + dx[direction] #이동 후 좌표
        time += 1

        if 1 <= mx and mx <= n and 1 <= my and my <= n and map_data[my][mx] != 1:
            x,y = mx, my
            map_data[my][mx] = 1

            # 사과 유무 확인
            if apple_array[my][mx] == 1 :
                apple_array[my][mx] = 0

                q.append((my,mx))

            elif apple_array[my][mx] == 0 :

                q.append((my,mx))
                py, px = q.pop(0)
                map_data[py][px] = 0
            
        else :   
            break

        if index < l and time == info[index][0] :
            direction = Rotation(info[index][1],direction)
            index += 1   

    return time

print(program())