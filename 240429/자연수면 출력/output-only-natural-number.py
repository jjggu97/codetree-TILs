num = input().split(' ')

a,b = int(num[0]),int(num[1])

if a >= 0:
    for i in range(b):
        print(a,end='')

if a < 1:
    print("0")