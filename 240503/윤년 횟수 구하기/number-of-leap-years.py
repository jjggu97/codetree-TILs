n = int(input())

cnt = 0

for i in range(1, n):
    if i % 4 == 0:
        cnt += 1

print(cnt)