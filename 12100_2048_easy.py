'''
새로운 값이 생기지 않는 2048 게임에서 
5번 이하로 움직이게 해서 나오는 최대값은? 
'''
# 중복순열을 이용해 나올수 있는 모든 경로를 찾는다.
# 틀리던 이유
# down과 right 함수에서 수의 범위를 -2부터 -n-1 로 짰었는데 
# 이럴 경우 DFS 함수에서 nx<0 ny<0 에 걸려버려서 움직임이 아예 x 
# 따라서 down,right함수에서 n-2부터 -1까지 -1을 차감하면서 순회하게 짰음


from itertools import product
from sys import stdin
from copy import deepcopy
input = stdin.readline 

ans = 0 
dx = [-1,0,1,0]  # up, left, down, right 
dy = [0,-1,0,1]
temp = [0,1,2,3]
paths = list(product(temp,repeat=5))

def DFS(x,y,dir,Graph,check):
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx<0 or ny<0 or nx>=n or ny>=n:
    return
  elif Graph[nx][ny] == 0:
    Graph[nx][ny],Graph[x][y] = Graph[x][y],0
    DFS(nx,ny,dir,Graph,check)
    return 
  elif Graph[nx][ny] == Graph[x][y] and check[nx][ny] == False:
    Graph[nx][ny], Graph[x][y] = Graph[nx][ny]*2, 0
    check[nx][ny] = True 
    return 
  else:
    return 

def upMove(graph):
  for j in range(n):
    c = [[False]*n for i in range(n)]
    for i in range(1,n):
      if graph[i][j] != 0 :
        DFS(i,j,0,graph,c)

def leftMove(graph):
  for i in range(n):
    c = [[False]*n for i in range(n)]
    for j in range(1,n):
      if graph[i][j] != 0 :
        DFS(i,j,1,graph,c)
      
def downMove(graph):
  for j in range(n):
    c = [[False]*n for i in range(n)]
    for i in range(n-1,-1,-1):
      if graph[i][j] != 0 :
        DFS(i,j,2,graph,c)

def rightMove(graph):
  for i in range(n):
    c = [[False]*n for i in range(n)]
    for j in range(n-1,-1,-1):
      if graph[i][j] != 0 :
        DFS(i,j,3,graph,c)

if __name__ == '__main__':
  n = int(input().rstrip())
  gr = [[0]*n for i in range(n)]
  for i in range(n):
    gr[i] = list(map(int,input().rsplit()))
  for path in paths:
    copygraph = deepcopy(gr)
    for now in path:
      if now == 0:
        upMove(copygraph)
      elif now == 1:
        leftMove(copygraph)
      elif now == 2:
        downMove(copygraph)
      else:
        rightMove(copygraph)
    for i in range(n):
      ans = max(ans,max(copygraph[i]))

  print(ans)
