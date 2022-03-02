'''
문제
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 
각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 
예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.



히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

입력
입력은 테스트 케이스 여러 개로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. 
(1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 
이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 
왼쪽부터 오른쪽까지 순서대로 주어진다. 
모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.
'''
# [ 세그먼트를 이용 ]
# segment 함수 

# 세그먼트 트리에 구간을 절반씩 나누면서 최소 높이를 가진 인덱스를 트리에 저장함

# query 함수
# 이후 쿼리문을 통해 원하는 구간에서의 최소 높이를 가지는 인덱스를 도출함 
# 쿼리 함수는 딱 이 용도 - 최소 높이를 가지는 인덱스(트리 노드에 저장된 값) 도출

# calcu 함수
# 가장 큰 범위 (0~n-1) 에서부터 출발하여 쿼리를 이용해 최소 높이를 가지는 인덱스를 찾는다.
# 해당 인덱스를 제외한(이미 위에서 구했으니까) 좌우 면적에서 최소 높이를 가지는 인덱스들을 각각 찾으면서 재귀를 돌린다.
# 넓이를 구할때마다 비교해가면서 최종 결과값을 출력

# 메모리 초과가 떠서 재귀 횟수를 제한했더니 통과함

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = int(1e9)
while(True):
  arr = list(map(int,input().rsplit()))
  n = arr[0]
  if n == 0:
   break
  arr = arr[1:]
  tree = [0]*(n*4) # 배열 길이 n 이상인 수 중에서 (제곱수+1)^2가 트리의 길이가 되는데 편의상 4를 곱함 
                    # n 이 7 이라면 가장 가까운 제곱수 9 -> 3 => (3+1)^2 = 16 
  s = 0 
  e = len(arr)-1
  
  def segment(start,end,node):
    global arr 
    global tree 
    
    if start>end:
      return 
    if end<0 or start>n:
      return 
    if start==end:
      tree[node] = start
      return 
    tree[node] = arr.index(min(arr[start:end+1]),start)   # index의 범위를 두지 않으면 동일 값을 가지는 인덱스가 나올수 있음
    mid = (start+end)//2
    segment(start,mid,node*2)
    segment(mid+1,end,node*2+1)
  
  segment(s,e,1)
  
  def query(start,end,left,right,node): 
    if right<start or left>end:
      return INF
    if left<=start and right>=end:
      return tree[node]
    mid = (start+end)//2
    left_index = query(start,mid,left,right,node*2)
    right_index = query(mid+1,end,left,right,node*2+1)
    if [left_index,right_index] == [INF,INF]:
      return 0
    if left_index == INF:
      return right_index 
    if right_index == INF:
      return left_index
    if arr[left_index]<arr[right_index]:
      return left_index 
    else:
      return right_index 
  
  ans = 0
  def calcu(left,right):
    global ans
    if left>right:
      return 
    stand = query(0,n-1,left,right,1)
    mat = arr[stand]*(right-left+1)
    ans = max(ans,mat)
    calcu(left,stand-1)
    calcu(stand+1,right)
  calcu(0,n-1)
  print(ans)





#[시간초과] - 
# 트리에 다 절반씩 나누면서 최소 높이를 가지는 인덱스를 저장했지만 
# 최소 높이를 기준으로 분할하지 않고 0부터 끝까지 하나하나 최소 높이를 계산했었음
# 당연하게도 n*n 이 되므로 시간 초과가 뜸
import sys 
input = sys.stdin.readline
INF = int(1e9)+1
while(True):
  arr = list(map(int,input().rsplit()))
  n = arr[0]
  if n == 0:
    break
  arr = arr[1:]
  tree = [0]*(4*n+1)
  s = 0 
  e = len(arr)-1
  def segment(start,end,node):
    global arr 
    global tree
    if start>end:
      return 
    if start>(len(arr)-1) or end<0:
      return 
    if start==end:
      tree[node]=arr[start]
      return 
    mid = (start+end)//2   
    tree[node] = min(arr[start:(end+1)])
    segment(start,mid,node*2)
    segment(mid+1,end,node*2+1)
  
  segment(0,n-1,1)
  
  def sum_t(start,end,left,right,node):
    
    if right<start or left>end:
      return INF
    if start>end:
      return INF
    if start==end:
      return tree[node]
    if left<=start and end<=right:
      return tree[node]
    mid = (start+end)//2
    return min(sum_t(start,mid,left,right,node*2),sum_t(mid+1,end,left,right,node*2+1))
    
  result = 0
  num = INF
  for i in range(n):
    for j in range(i,n):
      num = min(num,sum_t(0,n-1,i,j,1))
      num = num*(j-i+1)
      result = max(result,num)
      num=INF
  print(result)
