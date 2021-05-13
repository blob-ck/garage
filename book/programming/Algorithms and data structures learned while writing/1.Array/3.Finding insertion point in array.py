# 배열에서 삽입 위치 찾기
# 관련 사이트
# https://leetcode.com/problems/search-insert-position/
# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/simple-search-4/

# 정렬된 배열과 목표값이 주어지는데,
# 목표값과 일치하는 요소가 있다면 해당 인덱스를 반환하고
# 목표값과 일치하는 요소가 없다면 정렬상태를 유지하도록 알맞은 인덱스를 반환
# 인덱스만 반환하면 됨

import sys
sys.maxsize
# 32비트로 설치했다면
# 2147483647 == 2^31 - 1 : 0 ~ 2147483647 -> 31비트

# 64비트로 설치했다면
# 9223372036854775807 == 2^63 - 1 : 0 ~ 9223372036854775807 -> 63비트

# 파이선은 maxsize 범위를 넘어서는 숫자를 사용해도 스택오버플로우가 없다.
# 시바 머야 어떻게 한건데


NUMS = [1, 3, 5, 6] 
TARGET = 4

# Idea 1
# Brute force
# 1. 배열의 각 요소를 인덱스 0부터 순회
# 2. 순회하면서 target의 값과 같거나 크면 순회 중단
# 3. 중단된 시점의 인덱스 반환
# 시간복잡도: O(N)
# 공간복잡도: O(1)
def findInsertionIndex_bf(nums, target):
  for i in range(0, len(nums)):
    if(nums[i] == target or nums[i] > target):
      return i

print(findInsertionIndex_bf(NUMS, TARGET))


# Idea 2
# [KEYWORD]정렬된, 탐색 => 이진탐색 Binary Search
# 1.배열 요소를 이진탐색으로 접근
# 2.일치하는 요소를 찾았다면 해당 인덱스 반환
# 3.못찾았다면 마지막으로 접근한 낮은 인덱스를 반환
# 시간복잡도: O(logN)
# 공간복잡도: O(1)
def findInsertionIndex_bs(nums, target):
  low = 0
  high = len(nums) - 1
  # (low + high)/2
  # == low/2 + low/2 - low/2 + high/2
  # == low -low/2 + high/2
  # == low + (high - low)/2
  # low 와 high를 합한 후 나누는 순서로 mid를 구할 때
  # 합하는 시점에서 stackOverFlow를 예방하기 위한 변형식

  while(low <= high):
    mid = int(low + (high - low)/2) # (low + high)/2
    if(target == nums[mid]):
      return mid
    if(target > nums[mid]):
      low = mid + 1
    else:
      high = mid - 1
  # 일치하는 값이 없다면 low > high가 되는 시점에서 루프종료, low반환
  return low

print(findInsertionIndex_bs(NUMS, TARGET))