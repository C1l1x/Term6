# Функция - приема два стринг и връща един стринг съдържащ двата разделени с 
# нтервал.
# разменя първите два символа на двата стринга.
# def mix_up(a, b):
# mix_up('mix', 'pod') # 'pox mid'
# mix_up('dog', 'dinner') # 'dig donner'
# mix_up('gnash', 'sport') # 'spash gnort'
# mix_up('pezzy', 'firm') # 'fizzy perm'

def mix_up(a, b):
    result = b[:2]+ a[2:] + ' '
    result += a[:2] + b[2:]
    print(result)

    
mix_up('mix', 'pod') # 'pox mid'
mix_up('dog', 'dinner') # 'dig donner'
mix_up('gnash', 'sport') # 'spash gnort'
mix_up('pezzy', 'firm') # 'fizzy perm'