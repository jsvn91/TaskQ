dict1 = {'a':2, 'b' : 1}
dict2 = {'a':2, 'b' : 3 , 'c':3}

print('normal',{**dict1,**dict2}.__contains__('a'))

final_dict = {}

for key in list(dict1.keys()) + list(dict2.keys()) :
    final_dict[key] = dict1.get(key,0)+dict2.get(key,0)

print(final_dict)

from collections import Counter

print(Counter({**dict1, **dict2}))
