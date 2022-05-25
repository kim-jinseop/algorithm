# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

result = []
def solution(n, build_frame):

    # map data 기둥, 보 유무 
    # 1은 기둥이 설치된 곳으로 기둥과 보를 설치할 수 있는 위치
    # 2는 보가 설치된 곳으로 기둥은 설치 할 수 있으며, 보는 y+2 가 '2' 일때 설치 가능

    for frame in build_frame :
        x,y = frame[0] , frame[1] # 가로, 세로
        a = frame[2] # 0: 기둥 or 1: 보
        b = frame[3] # 0: 삭제 or 1: 설치

        if b==1 :
            result.append([x,y,a])
            if cheak(result) == False :
                result.remove([x,y,a])

        elif b==0 :
            result.remove([x,y,a])
            if cheak(result) == False :
                result.append([x,y,a])

    return sorted(result)

def cheak(result):
    
    for x,y,item in result :
        if item == 0 : # 기둥
            # 바닥일 때, 보의 한쪽 끝일 때, 다른 기둥 위일 때
            if y==0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result :
                continue
            else :
                return False

        elif item == 1 : # 보
            # 기둥 위 일때, 오른쪽에 기둥이 있을때, 양쪽에 보가 있을 때 
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
                continue
            else :
                return False

    return True