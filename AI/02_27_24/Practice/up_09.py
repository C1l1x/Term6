# Функция - приема стринг, ако е дължина поне 3 добавя 'ing' в края.
# Освен ако не завършва на 'ing' тогава добавя 'ly'.
# ако стринга е с дължина < 3 не го променя
# def verbing(s):
# verbing('hail') # 'hailing'
# verbing('swiming') # 'swimingly'
# verbing('do') # 'do'

def verbing(s):
    result = ''
    string_len = len(s)
    if len(s) < 3:
        result += s
        print(result)
    elif s[string_len-3:] == "ing":
        result += s + "ly"
        print(result)
    else:
        result += s + "ing"
        print(result)


verbing('hail') # 'hailing'
verbing('swiming') # 'swimingly'
verbing('do') # 'do'