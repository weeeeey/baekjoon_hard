'''
start와 end를 입력 받아서 최단 거리를 구하고 경로까지 출력하는 문제
'''
# 최단거리 구하는 방식은 동일
# 백트래킹은 각각의 visit 리스트에 방문한 이전 노드를 입력시켜둠
# visit[end] 부터 시작해서 start나올때까지 반복 

# 계속 틀렸다고 뜨던 이유 
# 중복된 경로에 대한 값을 처리 안해줌
# 1->2로 가는 경로가 두개 있을경우 더 적은 가중치를 가진 경로만 따지면 되니까
# 현재 distance[cur] 보다 크면 그냥 continue 해주면 됨
# 이거 때문에 틀렸다고 뜨고 시간 초과 뜸
import heapq
from sys import stdin
input = stdin.readline 
INF = int(1e9)

n = int(input())
distance = [INF]*(n+1)
m = int(input())
gr = [[] for i in range(n+1)]
for i in range(m):
  a,b,c = map(int,input().rsplit())
  gr[a].append([b,c])

start, end = map(int,input().rsplit())
distance[start] = 0
visit = [-1]*(n+1)

q = []
heapq.heappush(q,(0,start))
while(q):
  dis, cur = heapq.heappop(q)
  if dis>distance[cur]:
        continue
  for temp in gr[cur]:
    next_n,cost = temp 
    c = dis+cost
    if distance[next_n]>c:
      distance[next_n] = c  
      heapq.heappush(q,(c,next_n))
      visit[next_n] = cur      


res = []
res.append(end)
t= end 
while(visit[t]!=-1):
  res.append(visit[t])
  t = visit[t]

print(distance[end])
print(len(res))

for i in res[::-1]:
  print(i, end = ' ')
