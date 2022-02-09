from collections import deque 

m,n = map(int,input().split())
gr = [[] for i in range(n)]
dirty = 0
q = deque()
for i in range(n):
  gr[i] = list(input())
  for j in range(m):
    if gr[i][j] == 'o':
      gr[i][j] = '.'
      q.append((0,i,j)) #거리 , 청소한 방 개수, x,y
    if gr[i][j] == '*':
      dirty+=1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0 
visit = [[-1]*m for i in range(n)]
visit[q[0][1]][q[0][2]] = 0
while(q):
  room, x, y = q.popleft()
  if room == dirty:
    print(result)
    exit()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx<0 or ny<0 or nx >=n or ny>=m:
      continue 
    if gr[nx][ny] == 'x':
      continue 
    if visit[nx][ny] != -1:
      continue 

    if gr[nx][ny] == '.':
      q.append((room,nx,ny))
      visit[nx][ny] = visit[x][y] + 1

    if gr[nx][ny] == '*':
      gr[nx][ny] = '.'
      visit[nx][ny] = visit[x][y]+1
      result += visit[nx][ny]
      print(result)
      q=deque()
      q.append((room+1,nx,ny))
      visit = [[-1]*m for i in range(n)]
      visit[nx][ny] = 0
