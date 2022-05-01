'''
좌표와 좌표가 이어진 다리를 주어졌을때
다리를 건너지 않고서는 만날 수 없는 소들의 쌍을 구하는 문제 

전체 쌍 - 다리를 건너지 않고도 만날수 있는 쌍 = 다리를 건너지 않고는 만날 수 없는 쌍

이 로직을 가지고 문제를 풀었는데 계속 틀렸음

계속 틀릴 이유는 없었는데 그래프를 만들때 단순하게 N+1 로 짜줌
여기에서 문제가 발생했음


'''

from sys import stdin
from collections import deque 
input = stdin.readline 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
noRoad = 0
total = 0
N,K,R = map(int,input().rsplit())
gr = [[0]*(N) for i in range(N)]
road = [[[[False]*N for i in range(N)]for j in range(N)] for k in range(N)]
cow = [[0,0] for i in range(K)]
for i in range(R):
  a,b,c,d = map(int,input().rsplit())
  a-=1
  b-=1
  c-=1
  d-=1
  road[a][b][c][d] = True 
  road[c][d][a][b] = True 
for i in range(K):
  a,b = map(int,input().rsplit())
  a-=1
  b-=1
  cow[i] = [a,b]
  gr[a][b] = i+1
for temp in cow:
  tx,ty = temp 
  sur = gr[tx][ty]
  visited = [[True]*N for i in range(N)]
  visited[tx][ty] = False 
  q = deque() 
  q.append((tx,ty))
  while(q):
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx>=N or ny>=N or visited[nx][ny]==False:
        continue 
      if road[x][y][nx][ny]==True:
        continue
      if gr[nx][ny] == 0:
        visited[nx][ny] = False 
        q.append((nx,ny))
      if gr[nx][ny] != 0:
        tar = gr[nx][ny]
        if tar>sur:
          noRoad+=1
        q.append((nx,ny))
        visited[nx][ny] = False 

for i in range(1,K):
  total+=i
print(total-noRoad)
