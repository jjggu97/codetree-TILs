cnt = 0
total = 0

while True:

    n = int(input())

    if n >= 30 or n <= 10:
        avg = total / cnt
        print(f'{avg:.2f}')
        break
    else:
        cnt += 1
        total += n