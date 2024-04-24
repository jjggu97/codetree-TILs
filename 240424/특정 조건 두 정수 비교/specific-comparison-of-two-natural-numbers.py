num = input().split(' ')

a, b = int(num[0]),int(num[1])

if a < b:
    print("1",end=" ")
else:
    print("0",end=" ")

if a == b:
    print("1")
else:
    print("0")