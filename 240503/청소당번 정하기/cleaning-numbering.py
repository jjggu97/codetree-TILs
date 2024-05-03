clean2 = 0
clean3 = 0
clean12 = 0

n = int(input())

for i in range(1, n + 1):

    if i % 12 == 0:
        clean12 += 1
    elif i % 3 == 0:
        clean3 += 1
    elif i % 2 == 0:
        clean2 += 1

print(clean2, clean3, clean12)