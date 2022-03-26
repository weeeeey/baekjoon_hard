'''
문제
어떤 N개의 수가 주어져 있다. 
그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다. 
만약에 1, 2, 3, 4, 5 라는 수가 있고, 
3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다.
그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000),
K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고,
K는 구간의 곱을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 
그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데, 
a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
예제 출력 1 
240
48
예제 입력 2 
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 3 6
2 2 5
예제 출력 2 
0
240
'''
# 문제를 보자마자 세그먼트 트리를 이용해 구간 곱들을 저장해놔야겠다고 생각함
# [주의점]
# 특정 인덱스의 값을 0 으로 변경할시 그 이후 값을 수정할때 이전 값들을 모조리 까먹어서 아웃됨
# 이 점은 예시를 통해 알게 되어 리프 부터 변경하면서 부모 노드 값을 좌우 곱으로 하면 되겠다고 유추함

# [시간 초과 뜬 이유]
# 1. 세그먼트 트리르 초기화 할 때 바보 같이 그 안에서 O(n) 만큼 곱셍 값을 구한 뒤 밑에 값들로 나아감
# - 윗 대가리부터 구하는게 아니라 위에서부터 시작해서 리프까지 간 다음에 값을 저장해 둔 뒤 
# 노드를 채워 나가면 됐음

# 2. 값을 출력할때 1e9+7 로 나눈 나머지를 출력하라길래 그렇구나 하고 했는데
# (a*b)%c 는 a%c*b%c 이므로 트리에 저장 시켜줄때 애초에 나머지를 저장해두면 됨
# 계속해서 큰 값을 가지고 다니기에는 무겁기 때문에 시간 초과가 뜨는거 
# 수정하니까 맞음


from sys import stdin
input = stdin.readline 
INF = (int(1e9)+7)

def segment(start,end,node):
  if start==end:
    s[node]=arr[start]
    return s[node]
   
  m = (start+end)//2
  s[node]=segment(start,m,2*node)*segment(m+1,end,(2*node)+1)%INF
  return s[node]
  
def calcu(start,end,left,right,node):
  if right<start or left>end:
    return 1 
  if left<=start and right>=end:
    return s[node]
  m = (start+end)//2
  
  return calcu(start,m,left,right,2*node)*calcu(m+1,end,left,right,(2*node)+1)%INF
  

def update(start,end,num,cha,node):
  if num<start or num>end:
    return 
  if start==end:
    s[node] = cha
    return 
  mid = (start+end)//2
  update(start,mid,num,cha,2*node)
  update(mid+1,end,num,cha,2*node+1)
  s[node] = s[2*node]*s[2*node+1]%INF

if __name__=='__main__':
  n,m,k = map(int,input().rsplit())
  arr = []
  for i in range(n):
    arr.append(int(input().rstrip()))
  s = [-1]*(n*4)
  
  segment(0,n-1,1)
  
  for i in range(m+k):
    a,b,c = map(int,input().rsplit())
    if a==1:
      
      arr[b-1] = c
      update(0,n-1,b-1,c,1)
    else:
      print(calcu(0,n-1,b-1,c-1,1))
