num = input().split(' ')

a,b = int(num[0]),int(num[1])

total = 0

for i in range(a,b+1):
    if i % 2 == 0:
        total += i

print(total)