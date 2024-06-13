n = input().split(' ')
con = False
a,b,c = int(n[0]),int(n[1]),int(n[2])

for i in range(a,b+1):
    if i % c == 0:
        con = True
        break
    
    else:
        continue

if con == True:
    print('YES')

else:
    print('NO')