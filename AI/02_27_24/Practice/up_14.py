# Функция: приема число,
# и намира всички негови делители.

def find_divisors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    print(result)

find_divisors(12)
find_divisors(17)
find_divisors(30)
find_divisors(45)