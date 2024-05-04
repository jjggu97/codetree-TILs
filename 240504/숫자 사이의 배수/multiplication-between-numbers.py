sum = 0
cnt = 0

num = input().split(' ')

a,b = int(num[0]),int(num[1])

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        cnt += 1
    

avg = sum / cnt
avg = round(avg,1)

print(sum, avg)