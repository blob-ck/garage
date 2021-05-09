# 주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목표값을 만들 때
# 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램 작성
# 입력값으로 주어지는 배열에는 정확히 하나의 정답만 존재하며,
# 같은 요소의 값을 중복해서 사용할 수 없다.

# 입/출력 예시
# 입력: nums = [2, 7, 10, 19], target = 9
# 출력: [0, 1]

# 제한사항(Constraints)
# 1. 정수형 배열
# 2. 두 수의 합이 정수형을 초과하는 경우가 발생하는가?
#   - 문제에 언급 없음
# 3. 두 수의 합 값이 배열 내에 무조건 존재하는가?
#   - 정확히 하나의 해결책 존재
# 4. 중복된 요소의 값을 2번 이상 사용하여 결과값을 만들어서는 안된다.

# [KEYWORD]배열에서 중복값을 찾거나 순회하면서 특정값을 찾으려면 hashTable, set을 떠올리자
# TestCase를 만들 때도 제한사항을 확인하여 만들어야한다.
# [2, 3, 8, 9, 11, 12]의 경우 두 수의 합이 14인 경우가 [2, 12], [3, 11] 두 개이므로 결과값이 다르게 나옴
# 제한사항에 따라 유일한 조합인 경우만 TestCase로 사용해야함에 주의한다


# 아이디어 1
# Brute force
# 1. 배열의 모든 요소의 조합을 찾는다.
#   - 루프는 i=1~n, j=i+1~n으로 2중 루프 구성
#   - 루프1은 n번, 루프2는 n-1번 순회하므로 시간복잡도는 O(n^2)
#   - 공간복잡도는 O(1)
# 2. 해당조합으로 목표값과 비교하여 같다면 해당루프를 종료하고 인덱스조합 반환
# nums = [2, 7, 8, 11]
# target = 9
nums = [2, 3, 8, 9, 11]
target = 14
def twoSum_bf(nums, target):
  for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
      if (nums[i] + nums[j] == target):
        return [i, j]
  return [-1, -1]
print("Brute force solution result : ", twoSum_bf(nums, target))

# 아이디어 2
# Hash Table
# 1. 해시테이블을 구성한다
#   - key는 배열의 요소, value는 인덱스로 구성
# 2. 각 요소를 순회하면서
#   - 목표값 - 현재요소 = 다른요소
#   - 해시테이블에서 다른요소 값이 존재하는지 탐색
#   - 만약 다른요소가 해시테이블에 존재하면 현재요소의 인덱스와 다른요소의 인덱스를 반환
#   - 만약 다른요소가 해시테이블에 존재하지 않는다면, 현재요소를 해시테이블에 추가한다
#     해시테이블.추가({key:현재요소값, value:현재요소인덱스})
def twoSum_ht(nums, target):
  hashTable = {}
  for i in range(0, len(nums)):
    value = target - nums[i]
    if(hashTable.get(value) is not None and hashTable[value] != i):
      return sorted([i, hashTable[value]])
    
    hashTable[nums[i]] = i
  return [-1, -1]
print("Hash Table solution result : ", twoSum_ht(nums, target))