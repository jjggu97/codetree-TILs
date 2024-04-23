num = input().split(' ')

a = num[0]
b = num[1]

a, b = int(a), int(b)

c = a + b
d = a - b

c, d = float(c), float(d)

answer = c / d
answer = float(answer)
print("{:.2f}".format(answer))