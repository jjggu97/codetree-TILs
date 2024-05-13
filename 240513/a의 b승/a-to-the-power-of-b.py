num = input().split(' ')

a,b = int(num[0]),int(num[1])

c = 1

for i in range(1,b+1):
    c *= a

print(c)