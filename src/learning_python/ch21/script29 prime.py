# Упражнения части IV. Простые числа

def prime(y):
    if -1 <= y <= 1:
        print(y, 'not prime')
        return

    x = abs(y // 2)
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')


prime(13) # 13 is prime
prime(13.0) # 13.0 is prime
prime(15) # 15 has factor 5
prime(15.0) # 15.0 has factor 5.0
prime(-15.0) # -15.0 has factor 5.0
prime(0) # 0 not prime
prime(1) # 1 not prime
