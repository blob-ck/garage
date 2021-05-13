# 정렬된 배열의 병합
# 관련사이트
# https://leetcode.com/problems/merge-sorted-array/
# https://www.codechef.com/problems/CCCB03
# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

# 주어진 정렬된 두 배열(nums1, nums2)을 정렬을 유지하면서 병합
# nums1 과 nums2의 각각 m, n 개의 요소로 초기화 되어있다(배열크기가 아니라 요소개수, 빈 공간이 있을수 있음)
# nums1은 nums1과 nums2를 병합하기에 충분한 크기로 할당되어 있다(m + n개)
from typing import List

# ----------------------------------------------------------------------------------------------
# python 의 특징 : Slice Alignment
def append_list(in_list):
  # in_list = [3, 4] => 이 경우 파라미터로 넘어온 list_test는 [3, 4]가 될 것같지만
  # 일반대입으로 이루어지는 리트스 연산은 값에 의한 호출로 처리된다네
  # 즉, 함수 내에 값이 할당되는 순간 새로운 리스트를 생성하여 해당값을 처리
  # Slice로 접근하여 값을 처리하면 참조에 의한 호출처럼 동작하는데
  # 이를 Slice Alignment라 한다
  in_list[:] = [3, 4]
  print(in_list)
list_test = [2]

append_list(list_test)
print(list_test)

def append_obj(obj):
  print(obj)
  obj['a'] = 222
  print(obj)
obj_test = {'a' : 1, 'b': 2, 'c':[1,2,3]}
append_obj(obj_test)
# ----------------------------------------------------------------------------------------------


# Constraints
# 1.주어진 nums1, nums2의 요소들은 정렬되어있음
# 2.nums1은 요소 m개를 가지고 있다
# 3.nums2는 요소 n개를 가지고 있다
# 4.nums1 배열의 크기는 m+n 이다

NUMS1 = [1, 2, 3, 4, 5, 0, 0, 0]
NUMS2 = [2, 5, 6]
# Idea 1-1
# 1.nums2의 요소를 nums1의 확보된 추가 공간에 삽입
# 2.sorted() 사용
# 시간복잡도: O(NlogN) -> sorted는 TimSort를 사용한다. 자바, 스위프트도 사용
# 공간복잡도: O(N) -> sorted는 TimSort를 사용한다.
def merge11(nums1, nums2):
  startIndex = len(nums1) - len(nums2)
  for i in range(len(nums2)):
    nums1[startIndex + i] = nums2[i]
  return sorted(nums1)

print(merge11(NUMS1, NUMS2))


# Idea 1-2
# python의 음수 index사용 -> 변수하나 덜 사용했음
def merge12(nums1, nums2):
  for i in range(len(nums2)):
    nums1[-(i+1)] = nums2[i]
  return sorted(nums1)

print(merge12(NUMS1, NUMS2))

# Idea 1-3
def merge13(nums1: List[int], m: int, nums2: List[int], n:int) -> None:
  for i, v in enumerate(nums2):
    nums1[m + i] = v
    
  nums1[:] = sorted(nums1)

merge13(NUMS1, 3, NUMS2, 3)
print(NUMS1)


# Idea 2
# 1.nums1을 위한 인덱스 포인터 i, nums1의 마지막요소를 가리킴(m-1)
# 2.nums2르르 위한 인덱스 포인터 j, nums2의 마지막 요소를 가리킴(n-1)
# 3.삽입을 위한 포인터 k, nums2의 마지막 요소를 가리킴(m + n -1)
# 4.현재 i 와 j 의 값을 비교한다
# 5.비교하여 큰 쪽의 값을 k의 위치에 추가한다
#   k 는 1 감소
#   비교하여 큰 쪽 인덱스 값이 k 에 추가되었으므로 큰 쪽의 인덱스는 1 감소한다
# 6.i, j 중 하나라도 0보다 작아지면 비교 중지 ==> 루프 정지조건
def merge2(nums1, m, nums2, n):
  # 1.nums1을 위한 인덱스 포인터 i, nums1의 마지막요소를 가리킴(m-1)
  i = m - 1
  # 2.nums2르르 위한 인덱스 포인터 j, nums2의 마지막 요소를 가리킴(n-1)
  j = n - 1
  # 3.삽입을 위한 포인터 k, nums2의 마지막 요소를 가리킴(m + n -1)
  k = m + n -1

  # 6.i, j 중 하나라도 0보다 작아지면 비교 중지 ==> 루프 정지조건
  while(i >= 0 and j >= 0):
    # 4.현재 i 와 j 의 값을 비교한다
    # 5.비교하여 큰 쪽의 값을 k의 위치에 추가한다
    if(nums1[i] > nums2[j]):
      nums1[k] = nums1[i]
      i -= 1

    elif(nums1[i] < nums2[j]):
      nums1[k] = nums2[j]
      j -= 1
    
    # 책과는 다르게 값이 같은 경우도 처리했음
    else: # nums1[i] == nums2[j]
      nums1[k] = nums1[i]
      i -= 1
      k -= 1
      nums1[k] = nums2[j]
      j -= 1
      
    #   k 는 1 감소
    #   비교하여 큰 쪽 인덱스 값이 k 에 추가되었으므로 큰 쪽의 인덱스는 1 감소한다
    k -= 1

  # NUMS1 이 원소가 없을 때(0으로만 채워진 경우) 처리
  #   nums1[i] == nums2[j] 를 처리하면 하나의 while만으로 끝날줄 알았으나
  #   테스트케이스 중 nums1에 0만 채워진 경우를 넘기지 못했음
  while(j >= 0):
    nums1[k] = nums2[j]
    k -= 1
    j -= 1


merge2(NUMS1, 5, NUMS2, 3)
print(NUMS1)



# 여러 테스트 케이스
# 1. 빈 배열
NUMS1 =[1,2,3]
NUMS2 = []
merge2(NUMS1, 3, NUMS2, 0)
print(NUMS1)

# 2. NUMS1 이 원소가 없을 때(0으로만 채워진 경우)
NUMS1 =[0,0,0]
NUMS2 = [1,2,3]
merge2(NUMS1, 0, NUMS2, 3)
print(NUMS1)

# 3. 정렬할 필요가 없는 경우
NUMS1 =[1,2,3,0,0,0]
NUMS2 = [4,5,6]
merge2(NUMS1, 3, NUMS2, 3)
print(NUMS1)
