num = [int(input()) for i in range(10)]

cnt3 = 0
cnt5 = 0

for i in range(0,10):
    num[i] = int(num[i])

    if num[i] % 3 == 0:
        cnt3 += 1
    
    if num[i] % 5 == 0:
        cnt5 += 1

print(cnt3, cnt5)