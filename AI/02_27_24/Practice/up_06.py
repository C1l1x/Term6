# Функция - приема стринг и връща стринг съдържащ първите два и последните два 
# символа на първоначалния стринг.
# def both_ends(s):
# both_ends('spring') # 'spng'
# both_ends('Hello') # 'Helo'
# both_ends('a') # ''
# both_ends('xyz') # 'xyyz'

def both_ends(s):
    result = []
    if len(s) < 2:
        return result
    else:
        result = s[0] + s[1] + s[-2] + s[-1]
    return result

result1 = both_ends('spring') # 'spng'
result2 = both_ends('Hello') # 'Helo'
result3 = both_ends('a') # ''
result4 = both_ends('xyz') # 'xyyz'

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
print(f"Result 4: {result4}")
