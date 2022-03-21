'''
LCS 2 
최장 공통 부분 수열을 구하는 문제 
ACAYKP 와 CAPCAK가 주어졌을때
ACAK가 정답이 된다.
'''
# dp 를 통해서 구한다.
# 행과 열을 소스와 데스티니 문자열의 길이에 맞게 지정한 후 

# 만약 sur[i] == des[j] 라면 dp[i][j] = dp[i-1][j-1]+1 이 된다.
# 이전 길이의 최장 값에 +1 을 해준 결과

# 다를시 dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 이 된다.
# 현재 비교하는 단계에서 최장 길이를 항상 보장시켜주기 위하여 

# dp를 저장한 후 트래킹 하는 방식을 짜기 힘들었음
# 처음에는 check 그래프를 따로 만들어서 최장값이 갱신되는 구간을 기록해둘까 했음
# 메모리 낭비

# 최장값이 갱신되는 구간을 찾기
# i,j 를 기준으로 dp[i-1][j] 와 dp[i][j-1] 중에 같은 값이 있다면 
# dp[i][j]는 최장값으로 갱신된 곳이 아닌 다른 값이므로 갱신된 점이라는 것임.
# 즉 최장값을 추적하기 위해 근처값중 같은 값인 최장값으로 이동

# 만약 인접점에 같은 값(==최장값이 없다면 이 점은 i-1,j-1 에서 갱신된 것이므로 그 점으로 이동 
# 그리고 ans 리스트에 추가 시켜줌 
# 같은 방식으로 역추적 계속 진행하면 됨 .


from sys import stdin
from collections import deque 
input = stdin.readline 

sur = list(input().rstrip())
cmp = list(input().rstrip())
m= len(sur)
n = len(cmp)
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
  for j in range(1,m+1):
    if cmp[i-1] == sur[j-1]:
      dp[i][j] = dp[i-1][j-1]+1 
    else: 
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = []
q = deque()
q.append((n,m))
while(q): 
  x,y = q.popleft() 
  if x<1 or y<1:
    continue  
  if dp[x][y]<1:
    continue
  if dp[x-1][y] == dp[x][y]:
    q.append((x-1,y))
  elif dp[x][y-1] == dp[x][y]:
    q.append((x,y-1))
  else:
    ans.append(cmp[x-1])
    q.append((x-1,y-1))

ans.reverse()
print(len(ans))
for i in ans:
  print(i,end = '')

