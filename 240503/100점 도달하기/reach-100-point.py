n = int(input())

for i in range(n,101):
    if n >= 90:
        print("A",end=' ')
    else:
        if n >= 80:
            print("B",end=' ')
        else:
            if n >= 70:
                print("C",end=' ')
                else:
                    if n >= 60:
                        print("D",end=' ')
                    else:
                        print("F",end=' ')