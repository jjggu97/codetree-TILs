num = input().split(' ')

a,b = int(num[0]),int(num[1])

if a > -1:
    for i in range(b):
        print(a,end='')
else:
    print("0")