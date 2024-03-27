# Функция: приема списък от числа,
# връща списък само от четните числа.

def chetni_chisla(s):
    result = []
    for num in s:
        if num % 2 == 0:
            result.append(num)
    print(result)

    
chetni_chisla([1, 2, 3, 4, 5, 6, 7, 8, 9])
chetni_chisla([2, 4, 7, 11, 12, 16])
chetni_chisla([4, 15, 100, 2534, 43, 1])