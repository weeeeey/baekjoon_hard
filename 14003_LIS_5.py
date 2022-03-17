'''
bisect를 이용해서 지나온 경로를 출력하는 LIS 알고리즘
O(NlogN)
'''
# bisect(이진탐색)를 통해서 가장 긴 부분수열을 구할 수 있다.
# 일반적인 방법으로 bisect를 사용했을시 temp에 담겨진 값이 최장길이의 경로를 보장하지 않음
# 따라서 각각의 값들의 인덱스를 dp에 저장

# dp에는 현재 arr값이 temp의 어느 위치에 저장되어 있는지 기록해준다
# 이떄 temp[-1] 보다 크다면 그냥 temp에 추가시켜주면서 현재까지의 최장길이를 dp에 저장
# temp[-1]보다 작을시 temp에서의 어느 위치에 해당되는지를 dp에 저장 

# 이후 dp를 탐색하면서 최장길이에 맞춰서 순서대로 트래킹하면 됨.

from sys import stdin
from bisect import bisect_left
input = stdin.readline 
INF = int(1e9)

n = int(input())
arr = list(map(int,input().rsplit()))

dp = [1]*(n)
temp = [-INF]
longest = 0
for i in range(n):
  if temp[-1]<arr[i]:
    longest+=1
    temp.append(arr[i])
    dp[i] = longest 
  else:
    idx = bisect_left(temp,arr[i])
    dp[i] = idx 
    temp[idx] = arr[i]
ans = []
max_idx = dp.index(longest)
print(longest)
for i in range(max_idx-n,-n-1,-1):
  if dp[i]==longest:
    ans.append(arr[i])
    longest-=1
for i in range(-1,-len(ans)-1,-1):
  print(ans[i], end = ' ')
