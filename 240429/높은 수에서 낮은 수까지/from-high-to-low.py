num = input().split(' ')

a,b = int(num[0]),int(num[1])

if a > b:
    for i in range(a,b-1,-1):
        print(i,end=' ')

if a < b:
    for i in range(b,a-1,-1):
        print(i,end=' ')