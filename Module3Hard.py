data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_data_structure(data_structure):
    result = 0
    for item in data_structure:

        if type(item) == int:
            result += item
        elif type(item) == str:
            result += len(item)
        elif type(item) in [tuple, set, list]:
            result += sum_data_structure(item)
        elif type(item) == dict:
            result += sum_data_structure(item.values())
            result += sum_data_structure(item.keys())
    return result
result = sum_data_structure(data_structure)
print(result)