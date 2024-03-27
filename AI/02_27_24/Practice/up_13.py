# Функция: приема два списъка,
# връща списък с общите елементи на двата списъка.

def same_elements(a, b):
    result = []
    for element in a:
        if element in b:
            result.append(element)
        
    print(result)

same_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
same_elements(['apple', 'banana', 'orange'], ['banana', 'orange', 'kiwi'])
same_elements(['a', 'b', 'c'], ['x', 'y', 'z'])