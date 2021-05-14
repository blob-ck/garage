# 파스칼의 삼각형
# 관련 사이트
# https://www.hackerrank.com/challenges/pascals-triangle/problem
# https://leetcode.com/problems/pascals-triangle/

# 수학의 이항계수를 사용한다. 조합 사용하면 뭐 n차 다항식의 계수 구하기 쉬운거 있잖아 왜 그거
# (x + y)^0 => 1
# (x + y)^1 => 1 1
# (x + y)^2 => 1 2 1
# (x + y)^3 => 1 3 3 1
# (x + y)^4 => 1 4 6 4 1
# (x + y)^5 => 1 5 10 10 5 1
# .
# .
# .
from typing import List

def pascalTriangle(n:int) -> List[List[int]]:


  # 약속을 하자
  # n은 층을 나타낸다. 층은 마지막 배열의 원소개수와 같다. 각 내부배열의 인덱스 + 1 과 같다
  outterList = []
  if(n <= 0):
    return outterList
  
  for i in range(0, n):
    innerList = []
    for k in range(0, i+1):
      if(k == 0 or k == i):
        innerList.append(1)
      else:
        innerList.append(outterList[i-1][k] + outterList[i-1][k-1])

    outterList.append(innerList)
    print(innerList)
  
  return outterList
        
print(pascalTriangle(5))
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
