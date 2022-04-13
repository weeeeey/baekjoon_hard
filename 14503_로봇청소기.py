'''
문제
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 
1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 
청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 
지도의 북쪽에서부터 r번째, 서쪽에서부터 c번째로 위치한 칸은 (r, c)로 나타낼 수 있다.

로봇 청소기는 다음과 같이 작동한다.

현재 위치를 청소한다.
현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 
왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 그렇지 않을 경우, 
왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 
바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
입력
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. 
d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 
3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 
빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

출력
로봇 청소기가 청소하는 칸의 개수를 출력한다.

예제 입력 1 
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력 1 
1
예제 입력 2 
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
예제 출력 2 
57
'''
# 문제를 제대로 안읽음
# 후진하는 과정에서 청소했던 구간이면 접근 못한다고 생각해서 문제를 품
# 후진할 때 벽일때만 작동을 멈추는거임

from sys import stdin 
input = stdin.readline 
dx = [-1,0,1,0]  # 0:북, 1:동, 2:남, 3:서
dy = [0,1,0,-1]
roll = [3,0,1,2]  # 북->서, 동->북, 남->동, 서->남 
back = [2,3,0,1]  # 북->남, 동->서, 남->북, 서->동
ans = 1
def positionBack(dir,x,y):
  global ans 
  d = back[dir]
  nx = x + dx[d]
  ny = y + dy[d]
  if gr[nx][ny] == 0:
    if visited[nx][ny] == 0:
      visited[nx][ny] = 1
      ans+=1
    return [dir,nx,ny]
  else:
    return False

def positionLeft(dir,x,y,num):
  global ans 
  if num == 4:
    return positionBack(dir,x,y)
  d = roll[dir]
  nx = x + dx[d]
  ny = y + dy[d]
  if gr[nx][ny] == 0 and visited[nx][ny]==0:
    ans+=1 
    visited[nx][ny] = 1
    return [d,nx,ny]
  return positionLeft(d,x,y,num+1)

if __name__ == '__main__':
  n,m = map(int,input().rsplit())  #세로 가로
  r,c,direction = map(int,input().rsplit()) #x,y,dir
  gr = [[0]*m for i in range(n)]
  
  for i in range(n):
    gr[i] = list(map(int,input().rsplit()))  #0:빈칸, 1:벽 
  visited = [[0]*m for i in range(n)]
  visited[r][c] = 1
  while(True): 
    temp = positionLeft(direction,r,c,0)
    if temp == False:
      print(ans)
      break  
    else: 
      direction,r,c = temp
