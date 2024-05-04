n = int(input())
sum = 0

num = [int(input()) for i in range(n)]

for j in range(0,n):
    num[j] = int(num[j])
    if num[j] % 2 == 1 and num[j] % 3 == 0:
        sum += num[j]

print(sum)