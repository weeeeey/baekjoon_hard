'''
그래프 상에 주어진 정보를 통해 
출발문에서 도착문까지 중간중간 거울을 설치하여 도달한다고 가정 했을때
설치하는 가장 최소의 거울 개수를 출력하기
* : 빛 통과 x 
. : 빛 통과 
!: 거울 성치 가능 (거울은 45도로 설치됨) 

'''
# 문들의 정보를 통해 출발 점에서 부터 방향을 잡음 
# 딱히 어려운 점은 없었는데 
# 도착 지점에서의 최소값은 도착하는 방향에 따라 다 다르므로 
# 모든 과정이 끝난 뒤에 해당 점에서의 최소값을 출력했어야함 -> 이걸 안해서 틀림


from collections import deque 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
INF = 1e9

n = int(input())
gr = [[] for i in range(n)]
a = [] 
start = []
end = [] 

for i in range(n):
  gr[i] = list(input())
  for j in range(n):
    if gr[i][j] == '#':
      a.append([i,j])
      gr[i][j] = '.'
start = [a[0][0], a[0][1]]
end = [a[1][0], a[1][1]]

q = deque()
sx,sy = start 

visit = [[[INF,INF,INF,INF] for i in range(n)] for j in range(n)]
visit[sx][sy] = [0,0,0,0]

for i in range(4): # 출발점에서부터 해당 부근 값의 각 방향에 따른 방향값을 저장 해줌
  nx = sx + dx[i]
  ny = sy + dy[i]
  if nx<0 or ny<0 or nx>=n or ny>=n:
    continue 
  if gr[nx][ny] == '.':
    q.append((nx,ny,i))
    visit[nx][ny][i] = 0 
  if gr[nx][ny] == '!': # 출발 부근에 ! 가 있으면 직진할수도 꺽을수도 있으니까 체크 해줌
    for j in range(4):
      if [dx[i],dy[i]] == [(-1)*dx[j],(-1)*dy[j]]:
        continue 
      if i==j: 
        q.append((nx,ny,j))
        visit[nx][ny][j] = 0 
      else: 
        q.append((nx,ny,j))
        visit[nx][ny][j] = 1 

while(q):
  x,y,dir = q.popleft() 
  
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx < 0 or ny< 0 or nx>=n or ny>=n:
    continue 
  if gr[nx][ny] == '.' and visit[nx][ny][dir] > visit[x][y][dir]:
    visit[nx][ny][dir] = visit[x][y][dir] 
    q.append((nx,ny,dir))
  if gr[nx][ny] == '!':
    for i in range(4):
      if (dx[i],dy[i]) == ((-1)*dx[dir],(-1)*dy[dir]):
        continue 
      if i == dir and visit[nx][ny][dir] > visit[x][y][dir]: 
        visit[nx][ny][dir] = visit[x][y][dir]
        q.append((nx,ny,dir))
      elif visit[nx][ny][i] > visit[x][y][dir]+1: 
        visit[nx][ny][i] = visit[x][y][dir] + 1
        q.append((nx,ny,i))
  
print(min(visit[end[0]][end[1]]))
