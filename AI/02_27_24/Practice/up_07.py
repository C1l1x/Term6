# Функция - приема стринг и замества всички символи еднакви на първия с '*'
# def fix_start(s):
# fix_start('babble') # 'ba**le')
# fix_start('aardvark') # 'a*rdv*rk'
# fix_start('google') # 'goo*le'
# fix_start('donut') # 'donut'

def fix_start(s):
    result = s[0]
    ele = result
    result += s[1:].replace(ele, '*')
    return result

result1 = fix_start('babble') # 'ba**le')
result2 = fix_start('aardvark') # 'a*rdv*rk'
result3 = fix_start('google') # 'goo*le'
result4 = fix_start('donut') # 'donut'

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
print(f"Result 4: {result4}")