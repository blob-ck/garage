# 정렬된 배열에서 중복 제거
# 오름차순으로 정렬된 배열의 요소들을 중복 없이 단 한 번씩만 가질 수 있도록 주어진 배열을 "그대로(in-place)" 수정하고,
# 수정된 배열의 새로운 길이를 반환한다.

# 배열을 그대로 수정하라는 말은 배열을 새로 생성하여 반환하는게 아니라 입력받은 배열을 mutable하게 사용하라는 뜻

# Constraints
# 1. 정수형 배열
# 2. 입력으로 주어지는 배열의 길이는 0 일 수도 있음
# 3. 추가 배열 선언없이 입력 배열을 그대로 수정해야 함
# 4. 반환값은 정수이고, 배열의 길이보다 작거나 같다

nums = [0, 0, 0, 1, 1, 2, 2, 2, 2, 2]
# nums = [1, 2, 3, 4]
# nums = []

# Idea
def removeDuplicatedNumberAtList1(nums):
  if(len(nums) <= 0): return 0
  curr = nums[0]
  cnt = 1
  for i in range(1, len(nums)):
    if(curr != nums[i]):
      cnt += 1
      curr = nums[i]
      nums[i] = curr

  return cnt
print("result : ", removeDuplicatedNumberAtList1(nums))