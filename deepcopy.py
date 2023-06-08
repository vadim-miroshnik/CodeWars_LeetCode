# Сделать функцию deep_copy. Она должна создавать копию передаваемого в него объекта.
# Надо поддерживать как минимум три типа: list dict set.
# Естественно, не пользуясь встроенной функцией
def list_copier(obj: list) -> list:
    res = []
    for item in obj:
        res.append(deep_copy(item))
    return res


def dict_copier(obj: dict) -> dict:
    res = {}
    for key, value in obj.items():
        key_copy = deep_copy(key)
        value_copy = deep_copy(value)
        res[key_copy] = value_copy
    return res


def set_copier(obj: set) -> set:
    res = set()
    for item in obj:
        res.add(deep_copy(item))
    return res


COPIERS = {list: list_copier,
           dict: dict_copier,
           set: set_copier}


def deep_copy(obj):
    copier = COPIERS.get(type(obj))
    if copier:
        return copier(obj)
    else:
        return obj


list1 = [[1, 1], [2, 2], [3, 3]]
list2 = deep_copy(list1)
print(f"list orig - {id(list1)}")
print(f"list copy - {id(list2)}")
print(f"list 1 elem orig - {id(list1[0])}")
print(f"list 1 elem copy - {id(list2[0])}")

dict1 = {"vadim": 43, "john": 12, "anna": 35}
dict2 = deep_copy(dict1)
print(f"dict orig - {id(dict1)}")
print(f"dict copy - {id(dict2)}")

set1 = {1, 2, 3}
set2 = deep_copy(set1)
print(f"set orig - {id(set1)}")
print(f"set copy - {id(set2)}")
