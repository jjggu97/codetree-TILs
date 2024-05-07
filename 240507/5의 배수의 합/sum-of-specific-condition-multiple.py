num = input().split(' ')
a,b = int(num[0]), int(num[1])
sum = 0

for i in range(a,b):
    if i % 5 == 0:
        sum += i

print(sum)