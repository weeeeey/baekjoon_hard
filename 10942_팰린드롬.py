'''
팰린드롬이란 반대로 말해도 같은 수열인 것을 뜻한다.
m번의 질문을 통해 각각
a번부터 b번까지의 수열이 팰린드롬 이라면 1을 출력
아니라면 0을 출력
'''
# 만약 질문이 한번 이었다면 시간 초과는 없었을것
# 질문이 1백만번이므로 기록해 두는 방식을 택해야 한다는건 깨달음

# 처음 생각한건 바텀 다운 방식
# i=0부터 j=끝 번호부터 해서
# 그 중간 값을 mid로 잡고 
# mid를 중심으로 left-=1, right+=1 을 해주면서 비교
# dp[left+1][right-1] 이 거짓이라면 그 다음 dp는 다 거짓이라고 생각하고 계쏙 품
# 이 경우 n이 짝수일때와 홀수 일때 나눠져서 ㅎㅌㅊ

# 바텀 업
# 길이가 1 라면 그것은 항상 트루니까 1
# 길이가 2 라면 두 수가 같으면 트루, 아니면 펄스
# 길이가 3 이상부터는 [left+1][right-1]이 트루고 arr[left] == arr[right]라면 트루


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
visit = [[0]*n for i in range(n)]

for i in range(n):   #길이가 1
  visit[i][i] = 1 
for i in range(n-1): #길이가 2
  if arr[i] == arr[i+1]:
    visit[i][i+1] = 1 
    
for le in range(2,n): # 길이가 3 이상
  for i in range(n-le):    
    
    if arr[i]==arr[i+le] and visit[i+1][i+le-1]==1:
     visit[i][i+le] = 1

m = int(input())
for i in range(m):
  a, b = map(int,input().split())
  a-=1
  b-=1
  print(visit[a][b])
