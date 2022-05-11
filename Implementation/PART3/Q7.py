# lucky strike

n  = input()

length_half = len(n) // 2

sumL = 0
sumR = 0
for i in range(len(n)//2) :
    sumL = sumL + int(n[i])
    sumR = sumR + int(n[-(i+1)])

if sumR == sumL :
    print('LUCKY')
else :
    print('READY')