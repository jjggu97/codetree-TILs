a = input().split(' ')
b = input().split(' ')

a_age, a_sex = int(a[0]), str(a[1])
b_age, b_sex = int(b[0]), str(b[1])

a_info = 0
b_info = 0

if a_age >= 19 and a_sex == 'M':
    a_info = 1
else:
    a_info = 0

if b_age >= 19 and b_sex == 'M':
    b_info = 1
else:
    b_info = 0

if a_info == 1 or b_info == 1:
    print("1")
else:
    print("0")