'''
문제
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 
 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 
보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 
뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 
즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

예제 입력 1 
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
예제 출력 1 
9
예제 입력 2 
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
예제 출력 2 
21
'''

# 구현 문제
# 사과의 위치가 담겨진 gr 그래프와 뱀의 움직임을 나타내는 snake 그래프가 있다.
# 사과가 없을때는 꼬리를 한칸 땡겨야하는데 이것을 이전 방향값을 기역할려했다가 
# 움직임을 저장하는 것은 비효율적이므로 꼬리를 기점으로 네 방향에 대해 다음 칸인 것을 골라 이동시켜면 끝

# 방향이 바뀌는 것은 x초일때의 움직임 이후에 변하는 것을 주의
# 그 외에는 무난하게 해결 

from sys import stdin 

ans = 0 
input = stdin.readline 
dx = [0,-1,0,1]  # 0:left, 1:up, 2:right, 3:down 
dy = [-1,0,1,0]
toggle = [[3,1],[0,2],[1,3],[2,0]]  # [0]:'L' 일떄 ,[1]:'R'일때

def dirChange(nowdir,character):  # x초 후 어느 방향이 바뀌는 것인지 계산하는 함수 
  if character == 'L':
    return toggle[nowdir][0]
  else:
    return toggle[nowdir][1]

if __name__ == '__main__':
  n = int(input().rstrip())
  gr = [[0]*n for i in range(n)]  #사과 정보
  snake = [[-1]*n for i in range(n)] #뱀 움직임 정보
  m = int(input().rstrip())
  for i in range(m):
    a,b = map(int,input().rsplit())
    gr[a-1][b-1] = 1
  l = int(input().rstrip())
  change_infor = []   #x초 움직임 이후 어디로 방향 트는지에 대한 정보
  for i in range(l):
    a,b = input().rsplit()
    change_infor.append([int(a),b])
  pointer = 0 
  dir = 2 
  x,y = 0,0
  tx,ty = 0,0 
  snake[0][0] = 0
  while(True):  
    ans +=1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx<0 or ny<0 or nx>=n or ny>=n:  #벽
      break  
    if snake[nx][ny] != -1:    # 본인 몸통에 닿았을때
      break  
    if gr[nx][ny] == 0: # 사과 x 
      snake[nx][ny] = snake[x][y] + 1 
      x,y = nx,ny 
      for i in range(4):  #꼬리 땡겨주기
        ntx = tx + dx[i]
        nty = ty + dy[i]
        if ntx<0 or nty<0 or ntx>=n or nty>=n:
          continue 
        if snake[ntx][nty] == snake[tx][ty]+1:
          snake[tx][ty] = -1 
          tx,ty = ntx,nty
          break 
    elif gr[nx][ny] == 1: # 사과 o ( 헤드만 움직임 )
      gr[nx][ny] = 0
      snake[nx][ny] = snake[x][y]+1
      x,y = nx,ny
    if pointer<l and ans == change_infor[pointer][0]: #방향 바뀌는지 체크
      dir = dirChange(dir,change_infor[pointer][1])
      pointer +=1

  print(ans)
