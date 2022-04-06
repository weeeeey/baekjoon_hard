'''
구슬 탈출 문제에서 지나온 방향까지 같이 출력하는 문제
'''
# 배열을 그냥 할당시키면 소스와 데스티니 배열 둘 중 하나라도 변경시 
# 이후 과정에서 둘 다 변경 되어버림
# deepcopy 로 복사시 따로따로 놀기 가능
# 아마 일반적인 방법으로 할당했을시 주소값을 복사하게 되면서 영향을 끼치는거 같음

from collections import deque 
from sys import stdin 
from copy import deepcopy

input = stdin.readline 
INF = int(1e9)
ans = INF
dic_ans = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]
dc = ['L','U','R','D']

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
q.append((a,b,c,d,0,[]))

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
  rx,ry,bx,by,move,moving = q.popleft()
  if move>=10:
    continue
  for i in range(4):
    nrx,nry = ballRoll(rx,ry,i)
    nbx,nby = ballRoll(bx,by,i)
    temp = deepcopy(moving)     #deepcopy
    if [nbx,nby] == [11,11]:
      continue 
    if [nrx,nry] == [11,11]:
      if move+1<ans:
        ans = move+1
        temp.append(dc[i])
        dic_ans = deepcopy(temp)
      continue
    if [nrx,nry] == [nbx,nby]:
      if abs(nrx-rx)+abs(nry-ry)>abs(nbx-bx)+abs(nby-by):
        nrx -= dx[i]
        nry -= dy[i]
      else:
        nbx -= dx[i]
        nby -= dy[i]
    if [nrx,nry,nbx,nby,move+1] in visited:
      continue 
    temp.append(dc[i])
    q.append((nrx,nry,nbx,nby,move+1,temp))
    visited.append([nrx,nry,nbx,nby,move+1])

if ans == INF:
  print(-1)
else:
  print(ans)
  print(''.join(dic_ans))
