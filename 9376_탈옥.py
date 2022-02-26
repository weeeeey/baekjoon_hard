'''
문제
상근이는 감옥에서 죄수 두 명을 탈옥시켜야 한다. 이 감옥은 1층짜리 건물이고, 상근이는 방금 평면도를 얻었다.

평면도에는 모든 벽과 문이 나타나있고, 탈옥시켜야 하는 죄수의 위치도 나타나 있다. 감옥은 무인 감옥으로 죄수 두 명이 감옥에 있는 유일한 사람이다.

문은 중앙 제어실에서만 열 수 있다. 상근이는 특별한 기술을 이용해 제어실을 통하지 않고 문을 열려고 한다. 하지만, 문을 열려면 시간이 매우 많이 걸린다. 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 개수를 구하는 프로그램을 작성하시오. 문을 한 번 열면 계속 열린 상태로 있는다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

첫째 줄에는 평면도의 높이 h와 너비 w가 주어진다. (2 ≤ h, w ≤ 100) 다음 h개 줄에는 감옥의 평면도 정보가 주어지며, 빈 공간은 '.', 지나갈 수 없는 벽은 '*', 문은 '#', 죄수의 위치는 '$'이다.

상근이는 감옥 밖을 자유롭게 이동할 수 있고, 평면도에 표시된 죄수의 수는 항상 두 명이다. 각 죄수와 감옥의 바깥을 연결하는 경로가 항상 존재하는 경우만 입력으로 주어진다.

출력
각 테스트 케이스마다 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값을 출력한다.
'''
# 처음에는 탈옥수를 기점으로 다른 탈옥수까지의 최소 개수 + 벽까지의 최소 개수 를 생각함 
# 이럴 경우 중복 처리를 하는 것에 대한 조건을 세우기 힘들었음.
# 그래프 자체의 면적을 넓혀서 0,0 에서 출발하는 점과 
# 각 탈옥수들의 움직임을 구하는 솔루션을 얻게 됨

# 각 지점별로 BFS를 돌린후 모두 거쳐간 점일 경우를 찾음 ( 겹친 곳)
# 만약 이때의 점이 #이라면 세 지점이 모두 거쳤으니까 중복의 수를 줄이기 위해 -2를 함 
# 그 중에서의 최소값을 출력하면 됨
# '.' 부터 방문한다는 것을 위해 appendleft 를 한다는 점
# 힙으로 돌리는 것과 같은 효과 발휘 하지 않을까 싶음
from collections import deque 
import sys  
input = sys.stdin.readline 
num = int(input().rstrip())
while(num != 0):
  num-=1
  n,m = map(int, input().rsplit())
  gr = [['.']*(m+2) for i in range(n+2)]
  a =[]
  fir = [] 
  sec = []
  for i in range(1,n+1):
    gr[i][1:]=input().rstrip()
    gr[i].append('.')
    for j in range(m+2):
      if len(a)!=2 and gr[i][j] == '$':
        a.append([i,j])
        gr[i][j] = '.'
  fir = a.pop()
  sec = a.pop()
  
  visit = [[[-1,-1,-1] for i in range(m+2)] for j in range(n+2)]
  
  def BFS(a,b,c):
    global gr 
    global visit  
    global n 
    global m
    q = deque()
    q.append((a,b))
    visit[a][b][c] = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while(q):
      x,y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=(n+2) or ny>=(m+2):
          continue  
        if gr[nx][ny] == '*':
          continue  
        if visit[nx][ny][c] != -1:
          continue 
        if gr[nx][ny] == '.':
          q.appendleft((nx,ny))
          visit[nx][ny][c] = visit[x][y][c]
        if gr[nx][ny] == '#':
          q.append((nx,ny))
          visit[nx][ny][c] = visit[x][y][c]+1
  
  ans = 10001
  BFS(0,0,0)
  BFS(fir[0],fir[1],1)
  BFS(sec[0],sec[1],2)
  
  for i in range(1,n+1):
    for j in range(1,m+1):
      if visit[i][j][0] != -1 and visit[i][j][1] != -1 and visit[i][j][2] != -1 :
        cnt = sum(visit[i][j])
        if gr[i][j] == '#':
          cnt-=2
        ans =min(ans,cnt)
  
  print(ans)
