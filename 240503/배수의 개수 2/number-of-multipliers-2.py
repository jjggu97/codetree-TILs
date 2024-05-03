cnt = 0

num = [int(input()) for i in range(10)]

for j in range(0,10):
    
    num[j] = int(num[j])

    if num[j] % 2 == 1:
        cnt += 1

print(cnt)