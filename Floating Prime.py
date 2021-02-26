def is_prime(n):
    # ไม่เช็ค 2 , 3 เพราะไม่มีทางเข้ามาได้
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


while True:
    x = float(input())
    if x == 0:
        break
    for i in range(1, 4):
        y = int(x * 10 ** i)
        if is_prime(y):
            print('TRUE')
            break
        if i == 3:
            print('FALSE')
            break





