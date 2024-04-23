num = input().split(' ')

a = num[0]
b = num[1]

a, b = int(a), int(b)

a += b
b += a
print(f"{a} {b}")