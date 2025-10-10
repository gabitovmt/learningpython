# Упражнения части IV. Словарные инструменты

def copyDict(dict):
    new_dict = {}
    for key in dict:
        new_dict[key] = dict[key]
    return new_dict


print({'last_name': 'G', 'first_name': 'M'})  # {'last_name': 'G', 'first_name': 'M'}


def addDict(dict1, dict2):
    new_dict = {}
    for key in dict1:
        new_dict[key] = dict1[key]
    for key in dict2:
        new_dict[key] = dict2[key]
    return new_dict


print(addDict({'last_name': 'G'}, {'first_name': 'M'}))  # {'last_name': 'G', 'first_name': 'M'}
# print(addDict(['G'], ['M']))  TypeError


def add(a, b):
    if type(a) == dict:
        return addDict(a, b)
    acc = []
    acc.extend(a)
    acc.extend(b)
    return acc


print(add({'last_name': 'G'}, {'first_name': 'M'}))  # {'last_name': 'G', 'first_name': 'M'}
print(add(['G'], ['M']))  # ['G', 'M']
