'''
정수를 하나씩 입력할때마다 불려진 수들의 중간값을 출력하는 프로그램을 짜야함
1.5.2.10.-99,7 을 입력했다면
1,1,2,2,2,2,5 를 출력
(짝수개라면 중간에 있는 두 수 중에서 작은 수를 출력.)
'''
# 처음에는 한번씩 입력할 때마다 정렬을 반복하여 중간값을 출력함 -> 시간 초과
# 입력할때마다 bisiect.insort_left 를 반복하여 출력함 -> 시간 초과
# 고민하던 중 중간값을 기준으로 그보다 작다면 left 힙에 크다면 right힙에 두어서
# 입력한 방향에 따라 l+=1 , r+=1 을 해줌
# 이때 r과 l의 차이가 2 라면 기준 값을 l과 r에 따라 left 힙이나 right 힙에 
# 중간값을 넣어주고 둘 중 한곳에서 빼온 것을 중간값으로 설정함.
# 이럴 경우 처음부터 계속해서 작은 값을 입력해줄때 오류가 생김
# 솔류션을 찾아봄
# 두개 힙을 사용한다는 생각은 동일
# left 힙의 루트 노드가 중간값이라는 생각을 못함 (짝수개일때 둘 중 작은값이 중간값이므로 left에 활용
# left와 right의 길이를 입력할때마다 동일하게 만들어줌으로써
# left 루트가 중간값이 되도록 짠다.
# left의 루트(left중 가장 큰값 ==중간값) 가 right의 가장 작은 값인 루트보다 작다면 둘이 교체

import sys
import heapq
input = sys.stdin.readline
left = []
right = []
n = int(input())
result = []
for i in range(n):
  temp = int(input())
  if len(left) == len(right):
    heapq.heappush(left,(-1)*temp)
  else:
    heapq.heappush(right,temp)
  if right and ((-1)*left[0]) > right[0]:
    big = (-1)*heapq.heappop(left)
    small = heapq.heappop(right)
    heapq.heappush(right,big)
    heapq.heappush(left,small*(-1))
  result.append((-1)*left[0])

for i in result:
  print(i)
