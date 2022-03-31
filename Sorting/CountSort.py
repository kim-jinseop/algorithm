# 계수정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 
count = [0] * (max(array)+1) # 빈 list 생성 

for i in range(len(array)) : # 숫자 카운팅 -> count list 1씩 증가
    count[array[i]] += 1
    
for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end=' ')
    
  