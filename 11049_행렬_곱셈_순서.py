'''
문제
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 
행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 
입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 
정답은 231-1 보다 작거나 같은 자연수이다. 
또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.

예제 입력 1 
3
5 3
3 2
2 6
예제 출력 1 
90
'''
# 묶여지는 방법에 따라 값이 달라진다.
# 파일 합치기랑 같은 맥락으로 보고 크누스 최적화를 통해 중간 지점인 k 를 계산했지만 틀렸다고 뜸.
# 크누스 최적화를 적용하기 위해서는 조건들이 성립해야 하는데
# 이 문제는 사각 부등식과 단조성이 성립이 안됨.
# C(a,c)+C(b,d) <= C(a,d)+C(b,c) 성립 X
# C(b,c)<=C(a,d) 성립 X
# 계산 방법에 따라 계속해서 값이 변하기 때문 

# 따라서 k 값은 start,end 사이 전체를 돌리면서 찾아봐야함 

import sys
input = sys.stdin.readline 
INF = int(1e9)

n = int(input())
mat = [[0,0] for i in range(n+1)] #행렬 정보 입력
for i in range(n):
  mat[i] = list(map(int,input().rsplit()))

dp = [[0]*(n) for i in range(n)]  #i부터 j까지의 최소 연산 수를 저장
loc = [[[0,0] for j in range(n)] for i in range(n)] # i부터 j까지의 최소 연산이 성립할때 계산된 행렬 크기 저장
for i in range(n):
  loc[i][i] = [mat[i][0],mat[i][1]] #초기 값 저장해두기 (그래야 사용 가능)

def calcu(start,end): #dp 값을 계산함과 동시에 dp값을 리턴하는 함수
  if start == end:
    return 0 #start와 end가 같으면 그 행렬은 계산을 안한거시므로 0을 리턴 
  if dp[start][end] != 0: #한번 계산된 값은 또 계산할 필요 없이 리턴
    return dp[start][end] 
  ans = INF
  for k in range(start,end):  #calcu를 하는 이유는 행렬이 그 값이 되기까지의 연산 수 또한 더해줘야하므로
    temp = calcu(start,k)+calcu(k+1,end)+ loc[start][k][0]*loc[start][k][1]*loc[k+1][end][1] 
    if ans>temp:
      ans = temp 
      loc[start][end] = [loc[start][k][0],loc[k+1][end][1]]
  dp[start][end] = ans
  return ans 
calcu(0,n-1)
print(dp[0][n-1])
