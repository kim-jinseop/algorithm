# https://programmers.co.kr/learn/courses/30/lessons/60057 
# 위 링크에서 문제풀기

def solution(s):    
    length = len(s)
        
    for step in range(1,length//2+1) :
        L_group = s[0:step]
        for i in range(1,length,step) :
            R_group = s[step:]
            
            if L_group == R_group :
            
        
    return 