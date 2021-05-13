# 정렬된 배열의 병합 2
# 관련 사이트
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

# 정렬된 배열 nums1과 nums2가 주어지고, 각각의 크기는 m, n 이다 (m, n 은 1 이상)
# 정렬을 유지하면서 작은 순서대로 nums1부터 채우고 nums2를 채우자
# ex> nums1 = [1,3,5,7] , nums2 = [2,4,8] 로 주어진다면
# 결과는 nums1 = [1,2,3,4], nums2 =[5,7,8]

# Constraints
# 1.추가 배열 공간할당이 없다
# 2.nums1과 nums2의 크기는 제한이 없다
# 3.nums1과 nums2의 요소는 정렬되어 있다

from typing import List

# Idea 1
# Brute force
# 1.nums1을 순회
# 2.nums1의 요소와 nums2의 첫 요소와의 크기를 비교
# 3.nums1의 요소가 nums2의 첫 요소보다 크면
#   nums2의 첫번째 요소를 nums1의 비교했던 요소와 교체
#   변경된 nums2의 첫번째 요소와 다른 요소를 비교하며 nums2 재정렬
# 4.두 배열이 계속 정렬된 채로 nums1의 순회가 끝날 때까지 비교 및 교환 진행
def merge(nums1:List[int], nums2:List[int]) -> None:
  # 1.nums1을 순회
  for i, nums1_item in enumerate(nums1):
    # 2.nums1의 요소와 nums2의 첫 요소와의 크기를 비교
    # 3.nums1의 요소가 nums2의 첫 요소보다 크면
    if(nums1_item > nums2[0]):
      #   nums2의 첫번째 요소를 nums1의 비교했던 요소와 교체
      nums1[i] = nums2[0]
      nums2[0] = nums1_item

      #   변경된 nums2의 첫번째 요소와 다른 요소를 비교하며 nums2 재정렬
      # nums2[:] = sorted(nums2) ==> 아래 루프와 동일한 결과
      for k, item in enumerate(nums2[1:], start=1):
        if nums1_item >= item:
          nums2[k-1] = item # nums2[k]
          nums2[k] = nums1_item # nums2[k-1]

  # 4.두 배열이 계속 정렬된 채로 nums1의 순회가 끝날 때까지 비교 및 교환 진행

# TEST CASE - 두 배열이 한 개 이상의 요소를 가지므로 빈 배열은 테스트 안함
NUMS1 = [1,3,5,7]
NUMS2 = [2,4,6]
merge(NUMS1, NUMS2)
print('TEST 1 : ', NUMS1, NUMS2)
# TEST 1 :  [1, 2, 3, 4] [5, 6, 7]

NUMS1 = [5]
NUMS2 = [2,4,6]
merge(NUMS1, NUMS2)
print('TEST 2 : ', NUMS1, NUMS2)
# TEST 2 :  [2] [4, 5, 6]