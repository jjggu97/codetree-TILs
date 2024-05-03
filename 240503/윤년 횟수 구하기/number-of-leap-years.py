n = int(input())

cnt = 0

for i in range(1, n):
    if i % 100 == 0 and i % 400 == 1:
        cnt += 0

    elif i % 4 == 0:
        cnt += 1


print(cnt)