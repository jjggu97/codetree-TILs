a = input().split(' ')
b = input().split(' ')
c = input().split(' ')

a_sym = str(a[0])
a_tem = int(a[1])
b_sym = str(b[0])
b_tem = int(b[1])
c_sym = str(c[0])
c_tem = int(c[1])

status = int(0)

if a_sym == 'Y' and a_tem >= 37:
    status += 1

if b_sym == 'Y' and b_tem >= 37:
    status += 1

if c_sym == 'Y' and c_tem >= 37:
    status += 1

if status > 1:
    print("E")
else:
    print("N")