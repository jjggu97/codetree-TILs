c = input()
a = input()
b = input()

c = str(c)
a = float(a)
b = float(b)

a = round(a,2)
b = round(b,2)

print(c)
print("{:.2f}".format(a))
print("{:.2f}".format(b))