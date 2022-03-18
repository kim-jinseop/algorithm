#수학적 법칙을 사용해서 해결
n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort(reverse=True)

max = data[0]
max_2 = data[1]

result = (8//(k+1))*(max*k+max_2)+(8%(k+1)*max)

print("result:" + str(result))