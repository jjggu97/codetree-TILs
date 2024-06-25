def is_composite(n):
    if n <= 1:
        return False  
    if n == 2:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True  
    return False 


n = int(input())


if is_composite(n):
    print("C")
else:
    print("N")