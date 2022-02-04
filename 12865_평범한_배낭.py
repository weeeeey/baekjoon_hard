'''
n개의 물건이 그에 따른 무게와 물건의 가치가 주어졌을때
배낭에 담을수 있는 무게 한도 k 에 맞춰서 짐을 쌀때
최대 가치를 낼 수 있는 값은?
'''
# 처음에 풀때는 최단 거리를 반대로 해서 최대 무게 값을 넣으면 된다고 판단했었음
# 하지만 그 값이 항상 최대값을 보장하지는 않음
# BFS로 풀려고 했지만 그러기엔 시간 초과가 날거라고 생각
# dp 로 풀 생각을 했지만 dp[i] = max (현재 물건을 담았을때 + 이 물건을 담지 않았을떄의 최대값, 이 전 최대값)을 생각했지만
# 이 물건을 담지 않았을때의 최대값을 계속해서 저장해야할텐데 그것을 어떻게 저장 할 지 판단을 못섬
# dp 자체를 2차원 배열로 잡으면 모든 값을 저장했다가 사용 가능하다는 것을 알게됨
# 행은 물건의 가치들 (n개) , 열은 k(무게) 로 잡아서
# dp[i][j] = max( 현재 물건의 가치 + 배낭의 무게 - 현재 물건의 무게 ,  dp[현재 물건을 담지 않았을때][현재 배낭 무게])
# 이렇게 짜면 된다
# 냅색 알고리즘 
n,k = map(int,input().split())
arr = [(0,0)]
for i in range(n):
  arr.append(tuple(map(int,input().split())))
dp = [[0]*(k+1) for j in range(n+1)]

for i in range(1,n+1):
  for j in range(1,k+1):
    weight = arr[i][0]
    value = arr[i][1]
    if j<weight:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(value+dp[i-1][j-weight],dp[i-1][j])
print(dp[n][k])
