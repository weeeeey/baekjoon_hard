'''
최소 스패닝 트리

크루스칼 알고리즘 - 간선의 가중치를 기준으로 정보들을 오름차순으로 정렬한 후
방문 중인 start,end의 부모 노드를 비교한 후 같으면 순환이 되므로 넘겨주고 다를시
큰 값에 작은 값을 넣어줌 ( 이 때 넣는 장소는 루트 노드에 값들을 넣는 거임 )
'''

from sys import stdin
input = stdin.readline 
arr = [] 
v,e = map(int,input().rsplit())
for i in range(e):
  arr.append(list(map(int,input().rsplit())))

arr.sort(key=lambda x:x[2])
parent = [i for i in range(v+1)]
ans = 0

def u_find(tar):
  if parent[tar]==tar:
    return tar
  if parent[tar]!=tar:
    return u_find(parent[tar])
    
for temp in arr:
  start,end,dis = temp 
  us = u_find(start)
  ue = u_find(end)
  if us==ue:
    continue 
  if us>ue:
    parent[us]=ue #이 부분에서 
  else:
    parent[ue]=us 
  ans+=dis 
  
print(ans)
