# Функция: разделя стринг на две половини.
# връща: a-front + b-front + a-back + b-back
# def front_back(a, b):
# front_back('abcd', 'xy') # 'abxcdy'
# front_back('abcde', 'xyz') # 'abcxydez'
# front_back('Kitten', 'Donut') # 'KitDontenut'

def front_back(a, b):
    result = ''
    half_a = (len(a) + 1) // 2
    half_b = (len(b) + 1) // 2
    result += a[:half_a] + b[:half_b] + a[half_a:] + b[half_b:]
    print(result)



front_back('abcd', 'xy') # 'abxcdy'
front_back('abcde', 'xyz') # 'abcxydez'
front_back('Kitten', 'Donut') # 'KitDontenut'