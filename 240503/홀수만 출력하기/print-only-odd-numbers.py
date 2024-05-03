num = int(input())

N = [int(input()) for i in range (num)]

for i in range(0, num):
    N[i] = int(N[i])

    if N[i] % 2 == 1 and N[i] % 3 == 0:
        print(N[i])