year = int(input())

if year % 4 == 0:
    print("true")
else:
    if year % 100 == 0:
        print("true")
    else:
        print("false")