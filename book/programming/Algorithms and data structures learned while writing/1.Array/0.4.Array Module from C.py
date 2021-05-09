# 파이썬에서는 C에서 사용하는 배열 접근을 단순히 Wrapping하여 지원하는 Array모듈을 제공한다.
# (C/C++에서 사용하는 배열 접근을 그대로 제공하기 위한 모듈)
# 리스트는 여러 타입의 요소를 가질 수 있으나 Array는 한 번 설정한 타입의 요소만 추가/삭제 가능함

# Array모듈을 통한 초기화
# array 모듈을 arr로 호출하겠다
import array as arr

# 정수형 배열을 생성하고 초기값으로[1,2,3]을 가짐
# array.array(타입코드, 초기값)
int_array = arr.array('i', [1,2,3])

# TypeCode    C언어타입      Python타입    최소크기(바이트)
# 'b'       signed char         int           1
# 'B'       unsigned char       int           1
# 'u'       Py_UNICODE          unicode       2
#                               character     2
# 'h'       signed short        int           2
# 'H'       unsigned short      int           2
# 'i'       signed int          int           2
# 'I'       unsigned int        int           2
# 'l'       signed long         int           4
# 'L'       unsigned long       int           4
# 'q'       signed long long    int           8
# 'Q'       unsigned long long  int           8
# 'f'       float               float         4
# 'd'       double              float         8

int_arr = arr.array('i', [1, 2, 3])

print("elements in array: ", end = "")
for i in range(0, len(int_arr)):
  print(int_arr[i], end = " ")
print()

# 인덱스 1 위치에 값 4 추가
int_arr.insert(1, 4)
print("elements after insertion : ", end = " ")
for i in (int_arr):
  print(i, end = " ")
print()

# 배열 요소 중 값 1을 찾아 제거
int_arr.remove(1)
print("elements after delete \'1\' in array : ", end = " ")
for i in (int_arr):
  print(i, end = " ")
print()

int_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10]

# list의 요소를 배열로 변환
int_arr = arr.array('i', int_list)
print("elements in array : ")
for i in (int_arr):
  print(i, end=" ")
print()

# 배열내 값이 3인 요소 중 가장 처음 인덱스 출력
print("The index of 1st occurrnece of 3 is : ", end = " ")
print(int_arr.index(3))