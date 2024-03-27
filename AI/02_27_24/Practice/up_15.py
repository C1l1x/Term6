# Функция: приема число,
# намира всички по-малки прости числа.

def find_primes(num):
    result = []
    for i in range(2, num):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    print(result)

find_primes(12)
find_primes(17)
find_primes(30)
find_primes(45)