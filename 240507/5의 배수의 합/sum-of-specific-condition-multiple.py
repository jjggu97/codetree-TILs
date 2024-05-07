num = input().split(' ')
a,b = int(num[0]), int(num[1])

total = 0

if a > b:
    for i in range(a,b+1):
        if i % 5 == 0:
            total += i

else:
    for i in range(b,a+1):
        if i % 5 == 0:
            total += i


print(total)