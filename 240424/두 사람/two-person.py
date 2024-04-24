a = input().split(' ')
b = input().split(' ')

a_age, a_sex = int(a[0]), str(a[1])
b_age, b_sex = int(b[0]), str(b[1])

if a_age >= 19 or b_age >= 19 and a_sex == 'M' or b_sex == 'M':
    print("1")
else:
    print("0")