num = input().split(' ')
a,b = int(num[0]), int(num[1])

sum = 0

if a > b:
    for i in range(a,b+1):
        if i % 5 == 0:
            sum += i

else:
    for j in range(b,a+1):
        if j % 5 == 0:
            sum += j



print(sum)