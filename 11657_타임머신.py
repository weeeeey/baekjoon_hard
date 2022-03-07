'''
문제
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 
각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, 
C는 버스를 타고 이동하는데 걸리는 시간이다.
시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, 
C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다. 
둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다. 

출력
만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다. 
그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 
가장 빠른 시간을 순서대로 출력한다.
만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.

예제 입력 1 
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
예제 출력 1 
4
3
예제 입력 2 
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2
예제 출력 2 
-1
예제 입력 3 
3 2
1 2 4
1 2 3
예제 출력 3 
3
-1
'''
# 최단 경로 문제에서 음수 간선이 포함되어 있는 경우이다.
# 다익스트라를 이용할 경우 음수 간선이 포함되어 있는 루트를 돌지 않을수도 있을뿐더러 무한 순회하는 경로가 발생하게 되어 
# 최단 거리가 항상 정답을 보장하는 다익스트라로 해결할 수 없다.

# 벨만 포든 알고리즘 사용
# 벨만 포든 알고리즘은 정점이 v개 , 간선의 개수가 총 e개 일때 O(ve) 시간 복잡도를 가지는 알고리즘이다.
# 한번 돌때 모든 간선의 정보를 받아와야한다.

# 간선의 정보들을 모두 받아온다. 이때 그래프에 저장하는 것이 아닌 하나의 배열에 출반점,도착점,가중치를 저장.
# distance = [INF]*(v+1)개 할당 =>노드 번호가 1부터 시작하기 때문 
# 시작점이 1인 경우, distance[1] = 0 으로 설정
# 밑에 순회를 v-1번 반복
# 한번 순환할때 모든 간선의 정보들을 다 방문해본다.
# 1부터 시작해서 간선의 정보들을 한번씩 다 돌려본다면 방문한 점들중에서 다음 노드 방문 가능 (distance[current] != INF 라면)
# 값이 이 전 값보다 더 작다면 갱신

# v-1 번의 순회가 끝난후 한번 더 돌아봤을때 값이 달라진다면 음수 순회가 발생한 것 


from sys import stdin 
from copy import deepcopy
input = stdin.readline
INF = int(1e9)

v, e= map(int,input().rsplit())
inform = []
for i in range(e):
  a,b,c = map(int,input().rsplit())
  inform.append([a,b,c])
distance = [INF]*(v+1)
distance[1] = 0
for num in range(v-1):
  for node in range(e):
    current = inform[node][0]
    next_node = inform[node][1]
    cost = inform[node][2]
    if distance[current] != INF and distance[next_node]>distance[current]+cost:
      distance[next_node] = distance[current] + cost 
      
temp = deepcopy(distance)
ans = 0
for node in range(e):
  current = inform[node][0]
  next_node = inform[node][1]
  cost = inform[node][2]
  if distance[current] == INF:
    continue 
  if distance[next_node]>distance[current]+cost:
    ans = -1
    break
if ans == -1:
  print(-1)
else:
  for i in range(2,v+1):
    if distance[i] != INF:
      print(distance[i])
    else: 
      print(-1)
