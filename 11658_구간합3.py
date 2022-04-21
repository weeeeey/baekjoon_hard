'''
문제
N×N개의 수가 N×N 크기의 표에 채워져 있다. 
그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 
표의 i행 j열은 (i, j)로 나타낸다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7
여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이 된다. 
(2, 3)을 7로 바꾸고 (2, 2)부터 (3, 4)까지 합을 구하면 3+7+5+4+5+6=30 이 된다.

표에 채워져 있는 수와 변경하는 연산과 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

입력
첫째 줄에 표의 크기 N과 수행해야 하는 연산의 수 M이 주어진다. 
(1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 
둘째 줄부터 N개의 줄에는 표에 채워져있는 수가 1행부터 차례대로 주어진다. 
다음 M개의 줄에는 네 개의 정수 w, x, y, c 또는 다섯 개의 정수 w, x1, y1, x2, y2 가 주어진다. 
w = 0인 경우는 (x, y)를 c로 바꾸는 연산이고, 
w = 1인 경우는 (x1, y1)부터 (x2, y2)의 합을 구해 출력하는 연산이다. 
(1 ≤ c ≤ 1,000) 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다.

출력
w = 1인 입력마다 구한 합을 순서대로 한 줄에 하나씩 출력한다.

예제 입력 1 
4 5
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 2 2 3 4
0 2 3 7
1 2 2 3 4
0 3 4 5
1 3 4 3 4
예제 출력 1 
27
30
5
'''
# 처음에는 각 라인별로 세그먼트 트리를 만들어서 해당하는 라인에 대하여 값을 합하는 것을 구현함
# 이럴 경우 시간 초과가 발생 

# 시간을 줄이기 위해 구한 각 라인의 세그먼트 트리를 열을 기준으로 새로운 트리를 만들어줌
# 그것을 통해 y좌표들로 행을 구하고 그 행에 대하여 x 좌표들로 열을 찾은 뒤 출력하면 됨

# y좌표로 행을 구하는 함수를 만들고 해당하는 라인 별로 x로 열을 구하게 함 (update와 sum 둘 다 이런 로직을로 짬)
# 실패가 뜸 
# 구한 라인의 중복을 배제하더라도 실패가 뜸
# 디버깅 결과 update에서 문제가 있었음

# 새로 짰음
# 라인을 따로 찾는 과정을 없애고 
# 해당하는 라인을 먼저 찾은 뒤 바로 바로 그거에 맞는 열을 찾는 것으로 하니 맞음


from sys import stdin
input = stdin.readline 

def rowMerge(line,start,end,node): #각 행에 대한 세그먼트 트리 구현
  if start>end:
    return 0
  if start==end:
    lineSegment[line][node] = gr[line][start]
    return gr[line][start]
  mid = (start+end)//2
  leftNode = rowMerge(line,start,mid,node*2)
  rightNode = rowMerge(line,mid+1,end,node*2+1)
  lineSegment[line][node] = leftNode+rightNode
  return lineSegment[line][node]

def colMerge(line,start,end,node):  #위애서 구한 세그먼트를 각 열에 맞춰 새로운 트리 구현 
  if start>end:
    return 0 
  if start==end:
    colSegment[line][node] = lineSegment[start][line]
    return colSegment[line][node]
  mid = (start+end)//2 
  leftv = colMerge(line,start,mid,2*node)
  rightv = colMerge(line,mid+1,end,node*2+1)
  colSegment[line][node] = leftv + rightv 
  return colSegment[line][node]

def FindLine(x1,y1,x2,y2,start,end,line): #구간 별 합을 찾는 함수, y에(행) 대해 해당하면 x(열) 구하기
  if y2<start or y1>end:
    return 0
  if start>=y1 and end<=y2:
    return calcu(line,x1,x2,0,n-1,1)
  mid = (start+end)//2
  leftv = FindLine(x1,y1,x2,y2,start,mid,line*2)
  rightv = FindLine(x1,y1,x2,y2,mid+1,end,line*2+1)
  return leftv+rightv

def calcu(line,x1,x2,start,end,node): #합 리턴
  if x2<start or x1>end:
    return 0 
  if x1<=start and end<=x2:
    return colSegment[line][node]
  mid = (start+end)//2
  leftv = calcu(line,x1,x2,start,mid,2*node)
  rightv = calcu(line,x1,x2,mid+1,end,2*node+1)
  return leftv+rightv

def columnUpdate(line,x,c):
  cs,ce=0,n-1
  node = 1
  while(cs<=ce):
    cmid=(cs+ce)//2
    colSegment[line][node]+=c
    if cs==ce:
      return
    if x<=cmid:
      node*=2
      ce = cmid     
    else:
      node=node*2+1
      cs=cmid+1
      
def rowUpdate(x,y,c):
  rs,re=0,n-1
  line = 1
  while(rs<=re):
    rmid = (rs+re)//2
    columnUpdate(line,x,c)
    if rs==re:
      return
    if y<=rmid:
      re=rmid
      line*=2
    else:
      rs=rmid+1
      line=line*2+1

if __name__=='__main__':
  n,m = map(int,input().rsplit())
  lineSegment = [[0]*(4*n) for i in range(n)]
  gr = [[0]*n for i in range(n)]
  for i in range(n):
    gr[i] = list(map(int,input().rsplit()))
  for i in range(n):
    rowMerge(i,0,n-1,1)
  colSegment = [[0]*(4*n) for i in range(4*n)]
  
  for i in range(1,4*n):
    colMerge(i,0,n-1,1)
  
  for i in range(m):
    temp = list(map(int,input().rsplit()))
    for i in range(len(temp)):
      temp[i]-=1
    if temp[0]==-1:
      x,y,t = temp[1:4]
      t+=1
      ori=gr[x][y]
      gr[x][y]=t
      cha = t-ori
      rowUpdate(x,y,cha)
    else:
      ax,ay,bx,by = temp[1:5]
      if ay>by:
        ay,by=by,ay
      if ax>bx:
        ax,bx=bx,ax
      ans = FindLine(ax,ay,bx,by,0,n-1,1)
      print(ans)
