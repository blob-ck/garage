# 리스트 요소 추가 및 삭제
# 추가: [append(any), extend(iterable), insert(index, any)]
# 삭제: [remove(target), clear(), del List[index]]

# append(any)
py_list = [1, 2, 3, 4, 5]
py_list.append(6)
print(py_list)
# [1, 2, 3, 4, 5, 6]

# append(any)
py_list_1 = [1, 2, 3]
py_list_2 = [4, 5, 6]
py_list_1.append(py_list_2)
print(py_list_1)
# [1, 2, 3, [4, 5, 6]]


# extend(iterable)
py_list_1 = [1, 2, 3]
py_list_2 = [4, 5, 6]
py_list_1.extend(py_list_2)
print(py_list_1)
# [1, 2, 3, 4, 5, 6]


# insert(index, any)
py_list = [1, 2, 3]
py_list.insert(3, 4)
print(py_list)
# [1, 2, 3, 4]


# remove(target) - 제거대상이 여럿일 경우 가장 앞선 인덱스 요소 삭제
py_list = [1, 2, 3, 2, 4]
py_list.remove(2)
print(py_list)
# [1, 3, 2, 4]

# clear()
py_list = [1, 2, 3]
py_list.clear()
print(py_list)
# []

# del List[index]
py_list = [1, 2, 3]
del py_list[1]
print(py_list)
# [1, 3]
