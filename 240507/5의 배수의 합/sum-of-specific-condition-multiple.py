num = input().split(' ')
a, b = int(num[0]), int(num[1])

total_sum = 0

start = min(a, b)
end = max(a, b)

for i in range(start, end + 1):
    if i % 5 == 0:
        total_sum += i

print(total_sum)