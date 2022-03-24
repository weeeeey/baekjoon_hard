'''
문제
전기 회로에서 두 점을 전선으로 이을 때, 길이는 짧을 수록 좋다.

크기가 N×M인 비어있는 회로판에서 두 점 A1과 A2, 그리고 B1와 B2를 전선을 이용해서 이으려고 한다. 
전선은 항상 그리드의 수직, 수평선 위에 있어야 한다. 또, 두 직선은 접하면 안 된다. 
이 경우에 필요한 전선의 길이의 최솟값을 구하는 프로그램을 작성하시오. 
전선은 회로판 바깥으로 나갈 수 없다.

입력
첫째 줄에 회로판의 크기 N과 M이 주어진다. (2 ≤ N, M ≤ 100) 

다음 네 줄에는 A1, A2, B1, B2의 좌표가 주어진다. 
점의 좌표는 두 정수의 쌍으로 이루어져 있고, 
첫 번째 좌표는 0 이상 N 이하이며 두 번째 좌표는 0 이상 M 이하이다. 
어떤 점도 같은 위치에 있지 않다.

출력
A1과 A2, 그리고 B1과 B2를 연결하는데 필요한 전선의 길이의 최솟값을 출력한다. 
만약, 불가능한 경우에는 "IMPOSSIBLE"을 출력한다.

예제 입력 1 
6 6
2 1
5 4
4 0
4 5
예제 출력 1 
15
예제 입력 2 
6 3
2 3
4 0
0 2
6 1
예제 출력 2 
IMPOSSIBLE
'''

# 최소의 길이 = 최소값+최소값 
# 하나의 최소값을 정해두고 다른 곳에서 출발한 최소 거리를 더하기
# 하지만 하나의 경로의 최단거리를 고정해두고 다른 출발점에서의 최단 경로를 더하는 것이 항상 최단거리를
# 보장해주는지 의문 (3+6 과 4+5는 같은 값이니까?)
# 이것은 여전히 의문

# 일단 최단경로를 고정해두고 다른 출발점에서의 최단 거리가 최단 거리를 보장한다.
# 그런데 고정해두는 최단 경로가 뒤바뀌면 경로 자체들이 변하게 되므로 역도 계산해줘야함

from collections import deque 
from sys import stdin
input = stdin.readline

ans=int(1e9)
n,m = map(int,input().rsplit())

asx,asy = map(int,input().rsplit())
aex,aey = map(int,input().rsplit())
bsx,bsy = map(int,input().rsplit())
bex,bey = map(int,input().rsplit())

dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = int(1e9)
def BFS(fsx,fsy,fex,fey,ssx,ssy,sex,sey):
  visit = [[[-1,-1] for j in range(m+1)] for i in range(n+1)]  
  check = [[False]*(m+1) for i in range(n+1)]  
  q = deque()
  visit[fsx][fsy] = [n+1,m+1]
  check[fsx][fsy] = True 
  q.append((fsx,fsy,0))
  res = 0
  while(q):
    x,y,dis = q.popleft()
    if [x,y] == [fex,fey]:
      check[x][y] = True 
      x,y = visit[x][y]
      while([x,y]!=[fsx,fsy]):
        check[x][y]=True 
        x,y = visit[x][y]
      res = dis 
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx>n or ny>m:
        continue 
      if [nx,ny]==[ssx,ssy] or [nx,ny]==[sex,sey]:
        continue 
      if visit[nx][ny] == [-1,-1]:
        visit[nx][ny] = [x,y] 
        q.append((nx,ny,dis+1))
  q = deque()
  check[ssx][ssy] = True 
  q.append((ssx,ssy,0))
  
  while(q):
    x,y,dis = q.popleft()
    if [x,y] == [sex,sey]:
      res+=dis 
      return res
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx>n or ny>m:
        continue 
      if check[nx][ny] ==False:
        check[nx][ny] = True 
        q.append((nx,ny,dis+1))
  return int(1e9)
ans = min(ans,BFS(asx,asy,aex,aey,bsx,bsy,bex,bey))
ans = min(ans,BFS(bsx,bsy,bex,bey,asx,asy,aex,aey))

print(ans if ans!=int(1e9) else "IMPOSSIBLE")
