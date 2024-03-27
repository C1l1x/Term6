# Напишете функция, която приема списък от стрингове и намира
# броя на стринговете, които са с дължина >=2 и първия и последния символ съвпадат.
# def match_ends(words):
# match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) # 3
# match_ends(['', 'x', 'xy', 'xyx', 'xx']) # 2
# match_ends(['aaa', 'be', 'abc', 'hello']) # 1

def match_ends(words):
    count = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count

result1 = match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) # 3
result2 = match_ends(['', 'x', 'xy', 'xyx', 'xx']) # 2
result3 = match_ends(['aaa', 'be', 'abc', 'hello']) # 1

print(f"Result from first list is: {result1}")
print(f"Result from second list is: {result2}")
print(f"Result from third list is: {result3}")
