num = input().split(' ')
total = 0
a,b = int(num[0]),int(num[1])

for i in range(a,b+1):
    if i % 6 == 0 and i % 8 != 0:
        total += i


print(i)