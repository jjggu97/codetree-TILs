A_score = input().split(' ')
B_score = input().split(' ')

a_math, a_eng = int(A_score[0]),int(A_score[1])
b_math, b_eng = int(B_score[0]),int(B_score[1])

if a_math > b_math and a_eng > b_eng:
    print("1")
else:
    print("0")