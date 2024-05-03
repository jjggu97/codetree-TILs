n = int(input())

alert = [3,6,9]

for i in range(1, n + 1):

    if i % 3 == 0:
        print("0",end=' ')
    
    elif i in alert:
        print("0",end=' ')
    else:
        print(i,end=' ')