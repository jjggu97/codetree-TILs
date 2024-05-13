prod = 1

num = input().split(' ')

a,b = int(num[0]),int(num[1])

for i in range(a,b+1):
    prod *= i

print(prod)