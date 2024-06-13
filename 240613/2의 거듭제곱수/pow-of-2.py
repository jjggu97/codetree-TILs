n = int(input())
a = 1
b = 2

while True:

    if n > b:
        a += 1
        b *= 2
    
    if n == b:
        print(a)
        break