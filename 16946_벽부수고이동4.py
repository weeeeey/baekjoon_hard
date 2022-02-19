'''
[문제]
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.

각각의 벽에 대해서 다음을 구해보려고 한다.

벽을 부수고 이동할 수 있는 곳으로 변경한다.
그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

[입력]
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.

[출력]
맵의 형태로 정답을 출력한다. 원래 빈 칸인 곳은 0을 출력하고, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.
'''
# 일단 처음에 문제 이해부터 뭔 말인지 싶었다.
# n과 m이 1~1000 이므로 기본적으로 중복 생각 안한다면 시간 초과 뜰거라고 생각함.
# 0인 위치들을 처음부터 돌리면서 따로 담아줌
# 그것들을 돌리면서 같은 덩어리들끼리 얼음 개수 세주고 인접 1들에 그 값들을 더해줌 
# [시간 초과 뜬 이유]
# 일단 인접 1들을 담을때 중복 체크 하는 경우를 O(n) 으로 체크함 => 그래프 자체에 방문 체크를 했다면 더 가벼움
# 10으로 나눈 나머지 담는걸 안해줘서 틀렸다고 뜸 ㅎ
# 백조 하위호환?



from collections import deque 
import sys 
input = sys.stdin.readline 

n,m = map(int,input().rsplit())
gr = [[] for i in range(n)]

result = [['0']*m for i in range(n)] # 정답 출력 용도

for i in range(n):      
  gr[i]=list(input().rstrip())  # 그래프 입력
  for j in range(m):
    if gr[i][j] =='1':
      result[i][j] = '1'

def BFS(a,b):  
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  
  q = deque() 
  one = []      # 인접 벽(1) 담기 위한 용도
  
  q.append((a,b))
  t = 1     # 한 덩어리에 들어갈 총 개수 
  gr[a][b] = '-1' # 방문 체크
  
  while(q):
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx < n and 0<=ny<m:
        if gr[nx][ny] == '-1':
          continue 
        elif gr[nx][ny] == '0':  # 한 덩어리 내에 0 개수 체크
          t+=1
          gr[nx][ny] = '-1' # 방문 쳌
          q.append((nx,ny))
        
        elif gr[nx][ny] == '1' :  # 벽(1) 정보 담음
          one.append([nx,ny])  
          gr[nx][ny] = '-1'    
        

  for o in one: # 해당 덩어리 근접 벽들에 갯수 더해주기
    x,y = o 
    gr[x][y] = '1'
    result[x][y] = str((int(result[x][y])+t)%10)
    


for i in range(n):
  for j in range(m):
    if gr[i][j] == '0':
      BFS(i,j)
        

for i in range(n):        # 정답 출력
    print(''.join(map(str, result[i])))
