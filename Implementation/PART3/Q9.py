# https://programmers.co.kr/learn/courses/30/lessons/60057 
# 위 링크에서 문제풀기

def solution(s):    
    andwer = len(s)
    result = []

    for step in range(1,len(s)//2+1) :
        L_group = s[0:step]
        count = 1 
        char = ''

        for i in range(step,len(s),step) :
            R_group = s[i:i+step]

            if L_group == R_group :
                count += 1

            else :
                char += str(count) + L_group if count > 1 else L_group
                L_group = s[i:i+step]
                count = 1                        

        char += str(count) + L_group if count > 1 else L_group
        andwer = min(len(char),andwer)

    return andwer
