n = int(input())

a = [int(input()) for _ in range(n)]

total = 0

for j in range(0,n):
    a[j] = int(a[j])
    total += a[j]

avg = total / n
avg = round(avg,1)

print(total, avg)