num = input("두 개의 정수를 입력하세요: ").split(' ')
a, b = int(num[0]), int(num[1])

total_sum = 0

start = min(a, b)
end = max(a, b)

for i in range(start, end + 1):
    if i % 5 == 0:
        total_sum += i

print("5의 배수의 합:", total_sum)