list = input().split(' ')

c,n = str(list[0]),int(list[1])

if c == 'A':
    for i in range(1,n+1):
        print(i,end=' ')

if c == 'D':
    for i in range(n,0,-1):
        print(i,end=' ')