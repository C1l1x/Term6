# Напишете функция, която приема списък от стрингове и го връща сортиран,
# като всички стрингове започващи с 'x' са в началото.
# def front_x(words):
# front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) # ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
# front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) # ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
# front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) # ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

def front_x(words):
    x_words = [i for i in words if i.startswith('x')]
    other_words = [i for i in words if not i.startswith('x')]

    sorted_words = sorted(x_words) + sorted(other_words)

    print(sorted_words)

front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) # ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) # ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) # ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])