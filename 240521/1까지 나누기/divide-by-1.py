n = int(input())
div = n

for i in range(1,n+1):
    n /= i
    if n <= 1:
        print(i)
        break