a = ["a","f","bar","b","a","aaaaa"]
index = {a[i]:i for i in range(len(a))}
index = {'a': 4, 'f': 1, 'bar': 2, 'b': 3, 'aaaaa': 5}
print(index['f'])
