'''
로봇 청소기 위치에서부터 시작하여 더러운 방에 들르면 그 방은 꺠끗한 방으로 청소된다.
이때 필요한 이동 횟수의 최솟값은?
'''
# 처음에는 다익스트랄 생각해서 최단 거리 위치해 있는거에 도착하고 거기서 또 최단 거리에 도착하면 된다고 생각함.
# 하지만 이러한 점이 항상 최선의 수를 보장하지 않음
# 즉 방문하는 지점마다 이동거리는 다 다르므로 전체 이동할 수 있는 모든 경로를 따져줘야함
# 순열을 통해 모든 이동 가능한 경로를 구한 뒤 각각의 BFS를 돌려 이동 횟수를 체크했지만 시간 초과가 뜸
# 메모이제이션을 통해 각각의 더러운 방들끼리의 이동 횟수를 기록해둬야함
# 힘들었다.


from collections import deque
import itertools 
import sys
input = sys.stdin.readline

while(True):
  m,n = map(int,input().split())
  if (m,n) == (0,0):
    break
  dirty = []
  start = []
  gr = [[]for i in range(n)]
  for i in range(n):
    gr[i] = list(input().rstrip())
    for j in range(m):
      if gr[i][j] == 'o':
        start = [i,j]
        gr[i][j] = '.'
      if gr[i][j] == '*':
        dirty.append([i,j])
  temp = [0]*len(dirty)
  for i in range(len(temp)):
    temp[i] = i
  arr = list(itertools.permutations(temp,len(dirty)))
  distant = [0]*len(arr)
  
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  
  dist = [[[[[-1] for a in range(m)] for b in range(n)] for c in range(m)] for d in range(n)] 
  
  def memo():
    global gr 
    global dirty
    for i in range(len(dirty)):
      sx,sy = dirty[i][0] , dirty[i][1]
      visit = [[-1]*m for i in range(n)]
      visit[sx][sy] = 0 
      q = deque() 
      q.append((sx,sy))
      cnt = 0
      while(q):
        x,y = q.popleft()
        
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx<0 or ny<0 or nx>=n or ny>=m:
            continue  
          if gr[nx][ny] == 'x':
            continue 
          if visit[nx][ny] != -1:
            continue 
          if gr[nx][ny] =='.':
            q.append((nx,ny))
            visit[nx][ny] = visit[x][y] + 1
          if gr[nx][ny] == '*':
            q.append((nx,ny))
            visit[nx][ny] = visit[x][y] + 1
            dist[sx][sy][nx][ny] = visit[nx][ny]
            dist[nx][ny][sx][sy] = visit[nx][ny]
            cnt+=1
  
  def BFS_start():
    aa =[-1]*len(dirty)
    q = deque()
    q.append((start[0],start[1]))
    visit = [[-1]*m for i in range(n)]
    visit[start[0]][start[1]] = 0
    cnt = 0 
    while(q):
      x,y = q.popleft()
      if cnt == len(dirty):
        break 
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
          continue 
        if gr[nx][ny] == 'x':
          continue 
        if visit[nx][ny] != -1:
          continue 
        if gr[nx][ny] == '.':
          visit[nx][ny] = visit[x][y]+1
          q.append((nx,ny)) 
        if gr[nx][ny] == '*':
          visit[nx][ny] = visit[x][y] + 1
          q.append((nx,ny))
          i = dirty.index([nx,ny])
          aa[i] = visit[nx][ny]
          cnt+=1   
    for i in range(len(arr)):
      distant[i] = aa[arr[i][0]]
  
  BFS_start()
  if -1 in distant:
    print(-1)
    continue
  memo()
  for i in range(len(arr)):
    node = arr[i] 
    for j in range(len(node)-1):
      sx,sy = dirty[node[j]][0], dirty[node[j]][1] 
      tx,ty = dirty[node[j+1]][0], dirty[node[j+1]][1]
      
      distant[i] = distant[i] + dist[sx][sy][tx][ty] 
  print(min(distant))
      
