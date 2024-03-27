# Функция: намира първото срещане на подстринга 'not' и 'bad'.
# Ако 'bad' е след 'not' замества целия израз 'not'...'bad' със стринга 'good'
# def not_bad(s):
# not_bad('This movie is not so bad') # 'This movie is good'
# not_bad('This dinner is not that bad!') # 'This dinner is good!'
# not_bad('This tea is not hot') # 'This tea is not hot'
# not_bad("It's bad yet not") # "It's bad yet not"

def not_bad(s):
    result = ''
    index_not = s.find('not')
    index_bad = s.find('bad')
    if index_not != False and index_bad != False and index_bad > index_not:
        result += s[:index_not] + 'good' + s[index_bad + 3:]
        print(result)
    else:
        result = s
        print(result)


not_bad('This movie is not so bad') # 'This movie is good'
not_bad('This dinner is not that bad!') # 'This dinner is good!'
not_bad('This tea is not hot') # 'This tea is not hot'
not_bad("It's bad yet not") # "It's bad yet not"