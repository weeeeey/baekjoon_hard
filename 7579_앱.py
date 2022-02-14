'''
[문제]
스마트하게 해결하기 위한 프로그램을 작성해야 한다

현재 N개의 앱, A1, ..., AN이 활성화 되어 있다고 가정하자. 
이들 앱 Ai는 각각 mi 바이트만큼의 메모리를 사용하고 있다. 
또한, 앱 Ai를 비활성화한 후에 다시 실행하고자 할 경우, 추가적으로 들어가는 비용(시간 등)을 수치화 한 것을 ci 라고 하자.
이러한 상황에서 사용자가 새로운 앱 B를 실행하고자 하여, 추가로 M 바이트의 메모리가 필요하다고 하자. 
즉, 현재 활성화 되어 있는 앱 A1, ..., AN 중에서 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보해야 하는 것이다. 
여러분은 그 중에서 비활성화 했을 경우의 비용 ci의 합을 최소화하여 필요한 메모리 M 바이트를 확보하는 방법을 찾아야 한다

'''
# dp인거는 눈치 챘음
# 이 전에 저장했던 것들이 또 사용될 수 있기 때문에 2차원 dp로 짜야한다는것도 눈치챔
# 문제에서 요구하는 것이 M바이트 였기 때문에 열을 바이트로 체크함
# 그럴 경우 메모리 초과가 됨 ( M이 1천만 이하였기 때문에 n이 100이라 메모리 넘어섬 ) => 최대4GB
# 솔루션을 통해 열을 비용으로 된다는걸 알게 됨.
# 점화식도 다시 짜서 테케는 맞는데 80%에서 떴다고 뜸
# 솔루션 코드를 봐도 로직은 같은데 계쏙 틀려서 혹시나싶어 dp 선언할때 요소 값을 -1 에서 0으로 바꿈
# 그랬더니 맞음 
# 완탐에서나 -1로 두고 이전 요소에 영향을 받는 것들은 0 으로 두자 


import sys 
input = sys.stdin.readline 
n, m = map(int,input().split())
arr = list(map(int,input().split()))
temp = list(map(int,input().split()))
last = sum(temp)
dp = [[0]*(last+1) for i in range(n)]
for i in range(n):
  arr[i] = [arr[i],temp[i]]
  
for i in range(temp[0],last+1):
  dp[0][i] = arr[0][0]

for i in range(1,n):
  for j in range(last+1):
    if j <arr[i][1]:
      dp[i][j] = max(dp[i][j],dp[i-1][j])
    else: 
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][1]]+arr[i][0])

result = last 
for i in range(n):
  for j in range(last+1):
    if dp[i][j]>=m:
      result = min(result,j)
print(result)
  


