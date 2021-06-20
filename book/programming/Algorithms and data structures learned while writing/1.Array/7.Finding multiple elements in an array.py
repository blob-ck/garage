# 배열에서 다수의 요소 찾기
# 관련 사이트
# https://leetcode.com/problems/majority-element/
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1
# https://www.codechef.com/problems/MFREQ

# 정수형 배열이 주어졌을 때 다수의 요소를 찾아보자
# 다수의 요소는 배열 내에서 n/2번(floor(n/2))를 초과하여 나타나는 요소를 말한다
#   ex> 배열 요소 총 개수가 9개라면 n/2는 4.5다. 결국 5번 이상 나타나는 요소를 찾으면 된다
# 배열은 항상 개 이상의 요소를 가진다
# 다수의 수가 무조건 하나 존재한다고 가정한다

# Constraints
# 1.정수형 배열
# 2.배열은 1개 이상의 요소를 가진다
# 3.다수의 수는 무조건 하나가 존재한다