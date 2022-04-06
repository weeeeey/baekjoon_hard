'''
구슬 탈출 문제에서 굴린 횟수가 10번 이하라는 조건이 없어짐
방문 체크 배열에서 이동 횟수를 지워주면 성공~
'''

from collections import deque 
from sys import stdin 

input = stdin.readline 
INF = int(1e9)
ans = INF
dx = [0,-1,0,1]
dy = [-1,0,1,0]

n,m = map(int,input().rsplit())
gr = [[] for i in range(n)]
a,b,c,d = 0,0,0,0
for i in range(n):
  gr[i] = list(input().rstrip())
  for j in range(m):
    if gr[i][j] == 'R':
      a,b = i,j
      gr[i][j] = '.'
    if gr[i][j] == 'B':
      c,d = i,j 
      gr[i][j] = '.'
q = deque()
q.append((a,b,c,d,0))

def ballRoll(x,y,dir):
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx<0 or ny<0 or nx>=n or ny>=m:
    return [x,y]
  if gr[nx][ny] == '#':
    return [x,y]
  if gr[nx][ny] == '.':
    return ballRoll(nx,ny,dir)
  if gr[nx][ny] == 'O':
    return [11,11]

visited = []
while(q): 
  rx,ry,bx,by,move = q.popleft()
  
  for i in range(4):
    nrx,nry = ballRoll(rx,ry,i)
    nbx,nby = ballRoll(bx,by,i)
    if [nbx,nby] == [11,11]:
      continue 
    if [nrx,nry] == [11,11]:
      ans = min(ans,move+1)
      continue
    if [nrx,nry] == [nbx,nby]:
      if abs(nrx-rx)+abs(nry-ry)>abs(nbx-bx)+abs(nby-by):
        nrx -= dx[i]
        nry -= dy[i]
      else:
        nbx -= dx[i]
        nby -= dy[i]
    if [nrx,nry,nbx,nby] in visited:
      continue 
    q.append((nrx,nry,nbx,nby,move+1))
    visited.append([nrx,nry,nbx,nby])

print(ans if ans!=INF else -1)
