n = int(input())
total = 0
i = 1
while i < n:
    if n % i == 0:
        total += i
    i += 1

if total == n:
    print("P")
else:
    print("N")