'''
문제
n×n짜리의 배열이 하나 있다. 
이 배열의 (1, 1)에서 (n, n)까지 이동하려고 한다. 
이동할 때는 상, 하, 좌, 우의 네 인접한 칸으로만 이동할 수 있다.

이와 같이 이동하다 보면, 배열에서 몇 개의 수를 거쳐서 이동하게 된다. 
이동하기 위해 거쳐 간 수들 중 최댓값과 최솟값의 차이가 가장 작아지는 경우를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n(2 ≤ n ≤ 100)이 주어진다. 다음 n개의 줄에는 배열이 주어진다. 
배열의 각 수는 0보다 크거나 같고, 200보다 작거나 같은 정수이다.

출력
첫째 줄에 (최대 - 최소)가 가장 작아질 때의 그 값을 출력한다.

예제 입력 1 
5
1 1 3 6 8
1 2 2 5 5
4 4 0 3 3
8 0 2 3 4
4 3 0 2 1
예제 출력 1 
2
'''
# 이분탐색 + BFS
# 이분 탐색으로 기준값을 정한 뒤 n,n 까지 도달할 수 있는지를 체크 
# 만약 도달했다면 end를 mid-1로 정해준뒤 기준값을 줄여주고 다시 탐색
# 도달하지 못했다면 start를 mid+1로 정한 뒤 기준값을 늘려 다시 탐색 
# 최종 mid 값이 답이 된다. 

# 그래프 탐색시 최대값-최소값 = 기준값이므로 
# 최대값 = 최소값 + 기준값이 된다.
# 탐색시 최소값+기준값을 탐색할수 있는 최대 기준값으로 잡으면 그래프에서 다음 점이 이 값보다 작을 경우에만
# 큐에 담아주면 된다.
# 이것을 통해 탐색시 다음 점이 min보다 작은지max보다 큰지 따로 저장해둘 필요 x 
from collections import deque 
from sys import stdin 
input = stdin.readline
INF = 10000
ans = 100000
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def BFS(s,e):
  q = deque() 
  visit = [[False]*n for i in range(n)]
  visit[0][0]=True
  q.append((0,0))
  while(q):
    x, y = q.popleft()
    if [x,y] == [n-1,n-1]:
      return True 
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue 
      if s<=gr[nx][ny]<=e and visit[nx][ny]==False:
        q.append((nx,ny))
        visit[nx][ny] = True
  return False

  
if __name__ == '__main__':
  n = int(input().rstrip())
  gr = [[0]*n for i in range(n)]
  max_s = 0
  min_s = 100000
  for i in range(n):
    gr[i] = list(map(int,input().rsplit()))
    max_s = max(max_s,max(gr[i]))
    min_s = min(min_s,min(gr[i]))

  start =0
  end = max_s-min_s  
  while(start<=end):
    mid = (start+end)//2
    toggle = False 
    for i in range(min_s,max_s+1):
      if i<=gr[0][0]<=i+mid:
        toggle = BFS(i,i+mid)
        if (toggle):
          break

    if toggle:
      end = mid-1
      ans = min(ans,mid)
      
    else:
      start= mid+1 
      
  print(ans)
