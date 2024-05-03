n = input().split(' ')

a,b = int(n[0]),int(n[1])
print(a,end=' ')

while a < b:
    if a % 2 == 1:
        a *= 2
        print(a,end=' ')
    else:
        a += 3
        print(a,end=' ')