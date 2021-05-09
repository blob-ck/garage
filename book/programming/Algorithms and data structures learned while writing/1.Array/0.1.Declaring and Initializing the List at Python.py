# 파이썬에서 배열(리스트) 사용법

# 리스트 초기화
# 빈 리스트 선언
py_list_empty = []
print(py_list_empty)
# []

# 리스트 초기화
# 특정요소를 가진 리스트 선언
py_list = [1,2,3,4,5]
print(py_list)
# [1, 2, 3, 4, 5]

# 리스트 초기화
# 0을 10개 가지는 리스트 초기화1
py_list_zeros_1 = [0 for i in range(10)]
print(py_list_zeros_1)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 리스트 초기화
# 0을 10개 가지는 리스트 초기화2
py_list_zeros_2 = [0] * 10
print(py_list_zeros_2)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]