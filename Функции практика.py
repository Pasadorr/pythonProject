def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

print((find_max([1, 32, 54, 100, -34])))

def counter(list_):
    count = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            count += 1
    return count

print((counter([23, 46, 2, 0, 5, -1])))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))







