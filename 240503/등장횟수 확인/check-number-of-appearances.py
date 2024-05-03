num = [int(input()) for i in range(5)]
cnt = 0

for j in range(0,5):
    num[j] = int(num[j])

    if num[j] % 2 == 0:
        cnt += 1

print(cnt)