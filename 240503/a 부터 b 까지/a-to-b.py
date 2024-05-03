n = input().split(' ')

a,b = int(n[0]),int(n[1])

for i in range(a, b + 1):
    if i % 2 == 1:
        i *= 2
        print(i,end=' ')
    else:
        i += 3
        print(i,end=' ')