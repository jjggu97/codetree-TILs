num = [int(input()) for i in range(10)]
total = 0
cnt = 0

for j in range(10):
    num[j] = int(num[j])
    if -1 < num[j] < 201:
        total += num[j]
        cnt += 1


avg = total / cnt
avg = round(avg,1)

print(total, avg)