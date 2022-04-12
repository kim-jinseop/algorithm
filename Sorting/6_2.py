# 성적이 낮은 순서로 학생 출력하기

number = int(input())

student = []
for i in range(number) :
    input_data = input().split()
    student.append((input_data[0], int(input_data[1])))
    
    
student = sorted(student, key= lambda x: x[1])

for result in student :
    print(result[0], end=' ')