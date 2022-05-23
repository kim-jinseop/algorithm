# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061



def solution(n, build_frame):

    data = [[0]*n for _ in range(n)]

    result = []
    for frame in build_frame :
        x,y = frame[0] , frame[1]
        a = frame[2] # 0: 기둥 or 1: 보
        b = frame[3] # 0: 삭제 or 1: 설치

        if a==0 and b == 1:
            result.append([x,y,a])
        elif a==1 and b ==1:
            if 


    return 

def column(data):

    return

def 
