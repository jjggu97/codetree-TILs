num = input().split(' ')

a,b,c = int(num[0]),int(num[1]),int(num[2])

if a > b and a < c:
    print(a)
else:
    if a > c and a < b:
        print(a)
    else:
        if b > a and b < c:
            print(b)
        else:
            if b < a and b > c:
                print(b)
            else:
                if c > a and c < b:
                    print(c)
                else:
                    if c < a and c > b:
                        print(c)