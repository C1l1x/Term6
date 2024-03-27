# Функция - слива два сортирани списъка
# def linear_merge(list1, list2):
# linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) # ['aa', 'bb', 'cc', 'xx', 'zz']
# linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) # ['aa', 'bb', 'cc', 'xx', 'zz']
# linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) # ['aa', 'aa', 'aa', 'bb', 'bb']

def linear_merge(list1, list2):
    result = list1 + list2
    return sorted(result)

result1 = linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
result2 = linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
result3 = linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")