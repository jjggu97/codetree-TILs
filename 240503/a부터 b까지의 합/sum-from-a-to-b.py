num = input().split(' ')

a,b = int(num[0]),int(num[1])

sum = 0

for i in range(a,b+1):
    sum += i

print(sum)