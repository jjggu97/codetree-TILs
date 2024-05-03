n = input().split(' ')

a,b = int(n[0]),int(n[1])

while a <= b:

    print(a,end=' ')

    if a % 2 == 1:
        a *= 2
    else:
        a += 3