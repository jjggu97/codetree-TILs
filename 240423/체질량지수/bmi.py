num = input().split(' ')

h = int(num[0])
w = int(num[1])

b = int((10000 * w) / (h * h))

print(b)

if b > 24:
    print("Obesity")