# 1. 피보나치 함수를 재귀 함수로 구현 (탑다운)

# def fibo(x) :
#     print("f("+str(x)+")",end=" ")
#     if x==1 or x==2 :
#         return 1
#     return fibo(x-1) + fibo(x-2)

# print(fibo(6))

#------------------------------------------------
# 2. 메모이제이션 기법을 사용해서 해결 (탑다운)
# d = [0] * 100

# def fibo(x) :
#     print("f("+str(x)+")",end=" ")
#     if x==1 or x==2 :
#         return 1
    
#     if d[x] != 0 :
#         return d[x]

#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]


# print(fibo(6))

#------------------------------------------------
# 3.반복문을 사용한 피보나치 수열 (보텀업)

number = int(input())

d = [0] * (number+1)
d[1] = 1
d[2] = 1

for i in range(3,number+1) :
    d[i] = d[i-1] + d[i-2]    

print(d[number])