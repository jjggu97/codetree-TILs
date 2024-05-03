n = int(input())

for i in range(n,101):
    if n >= 90:
        print("A",end=' ')
    if n >= 80:
        print("B",end=' ')
    if n >= 70:
        print("C",end=' ')
    if n >= 60:
        print("D",end=' ')
    else:
        print("F",end=' ')