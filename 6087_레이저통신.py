...
n*m 그래프에서 C로 표시된 출발지와 도착지가 있다.
한 번 꺽을때마다 거울을 사용한다고 가정했을때
도착지점까지 사용될 거울의 개수를 출력
...
# 방문 그래프를 해당 좌표에 도착하는데 사용하는 네 방향으로 따주고 거기까지 도착하는데 사용된
# 거울의 개수를 표시함
# 90도로 꺽이는 거울이므로 해당 방향의 반대 방향은 갈 수 없음
# 위(-1,0) 일땐 아래(1,0)을 왼쪽(0,-1) 일땐 오른쪽 (0,1)을 못가므로
# dir_x *-1 , dir_y *-1 과 dx[i],dy[i] 같은지 판별 ( 같다면 반대 방향이므로 continue)
# 단순하게 visit[좌표][방향]이 방문 전이라면 체크 해줬지만, 그럴 경우 
# 한 좌표에 도달하는 여러 방향들 중 가장 적은 거울을 제일 먼저 방문한다는 조건을 만족 못함
# 방문할려는 좌표에서의 거울 값과 현재 방향에서 가지고 있는 거울 개수를 판단해서
# 많은 거울이라면 갱신해줌

from collections import deque
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
gr = [[]for i in range(n)] 
a = []
start = []
end = []
for i in range(n):
  gr[i] = list(input().rstrip())
  for j in range(m):
    if gr[i][j] == 'C':
      a.append([i,j])
start = a[0]
end = a[1]
result = []

dx = [1,-1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((start[0],start[1],4))
visit = [[[10001]*4 for i in range(m)] for j in range(n)]
visit[start[0]][start[1]] = [0,0,0,0]

#출발
x,y,dir_s=q.popleft()
for i in range(4):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx<0 or ny<0 or nx>=n or ny>=m:
    continue 
  if gr[nx][ny] == '*':
    continue 
  if gr[nx][ny] == 'C':
    print(0)
    exit() 
  if gr[nx][ny] == '.':
    q.append((nx,ny,i))
    visit[nx][ny][i] = 0

#출발점 근방에서부터 출발
while(q):
  x,y,dir = q.popleft()
  for i in range(4):
    if [dx[i],dy[i]] == [(-1)*dx[dir],(-1)*dy[dir]]:
      continue 
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or ny<0 or nx>=n or ny>=m:
      continue 
    if gr[nx][ny] == '*':
      continue 
    if gr[nx][ny] == '.':
      if i == dir and visit[x][y][i]<visit[nx][ny][i]:
        visit[nx][ny][i] = visit[x][y][dir]
        q.append((nx,ny,i))
      elif i!= dir and visit[x][y][dir] +1<visit[nx][ny][i]:
        visit[nx][ny][i] = visit[x][y][dir]+1
        q.append((nx,ny,i))
    if gr[nx][ny] == 'C':
      if i == dir and visit[x][y][i]<visit[nx][ny][i]:
        result.append(visit[x][y][dir])
      elif i!= dir and visit[x][y][dir] +1<visit[nx][ny][i]:
        result.append(visit[x][y][dir]+1)
print(min(result))
