'''
가장 긴 부분수열의 길이와 요소 값을 출력

'''
#O(n^2)
# dp에는 arr[i]가 마지막 요소 값으로 왔을 경우 가장 긴 부분수열의 길이를 넣어줌.
# 최대 길이를 가지는 부분수열을 알고 싶을떄는 dp에서의 최대 길이를 갖는 인덱스를 알아낸 후 
# 그 인덱스부터 -1 을 해가면서 dp에서 result-1, result-2, result-3, ... , 1 을 정답 리스트에 넣은 후
# 역순으로 출력하면 됨
from sys import stdin
input = stdin.readline 
INF = int(1e9)
n = int(input())
arr = list(map(int,input().rsplit()))
dp = [1]*(n)
for i in range(n):
  for j in range(i):
    if arr[i]>arr[j]:
      dp[i] = max(dp[i],dp[j]+1)
ans = []
max_dp = max(dp)   # 가장 긴 부분수열의 길이
max_idx = dp.index(max_dp)  # 가장 긴 부분수열을 이루게 하는 arr의 인덱스 값
while(max_idx>-1):
  if dp[max_idx] == max_dp:
    ans.append(arr[max_idx])
    max_dp-=1
  max_idx-=1

print(max(dp))
for i in range(-1,-(len(ans))-1,-1):
  print(ans[i],end=' ')
