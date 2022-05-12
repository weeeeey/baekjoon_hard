'''

문제

0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 
다음과 같은 연산을 K번 수행한다.

    1 ≤ i < j ≤ M인 i와 j를 고른다. 
    그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 
    이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.
입력

첫째 줄에 정수 N과 K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, 
K는 10보다 작거나 같은 자연수이다.
출력

첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 
만약 연산을 K번 할 수 없으면 -1을 출력한다.
예제 입력 1

16375 1

예제 출력 1

76315

예제 입력 2

132 3

예제 출력 2

312

예제 입력 3

432 1

예제 출력 3

423

예제 입력 4

90 4

예제 출력 4

-1

예제 입력 5

5 2

예제 출력 5

-1

예제 입력 6

436659 2

예제 출력 6

966354
'''
# 처음에는 가장 큰수가 맨 앞으로 오면 된다고 생각
# point와 highest를 설정하여 가장 큰 수 highest가 point에 위치한게 아니라면 출력
# 같을 경우 자릿수를 +1 or highest +1 를 할려고 했음

# 하지만 이럴 경우 최종적으로 가장 큰 수가 올 경우를 보장해주지 않음
# 따라서 모든 조합을 다 따져봐야함 

# 숫자가 교환되어지는 모든 경우의 수를 따져본 뒤 최종적으로 교환을 진행했을때 가장 큰 수를 출력하면 됨

# 어려웠던 점: 숫자를 스트링화, 스트링으로는 스왑이 안되어서 리스트를 각각 int화
#           int화를 했던것들을 다시 join으로 묶어주기
#           set에 대한 이해 ( 인덱스 접근 x , 추가할때는 단일원자add, 배열일 경우 update

from sys import stdin 
from itertools import combinations 
from collections import deque
from copy import deepcopy
input = stdin.readline 

n,k = map(int,input().rsplit())
n=str(n)
check = [[] for i in range(k+1)]
for i in range(k+1):
  check[i] = set(check[i])
check[0].add(int(n))
temp = [i for i in range(len(n))]
com = list(combinations(temp,2))
ans = -1

for num in range(1,k+1):
  q = deque()
  temp = list(check[num-1])
  for i in range(len(temp)):
    q.append(temp[i])
  while(q):
    number = q.popleft()
    number = list(str(number))
    for combination in com:
      arr = deepcopy(number)
      x,y = combination
      arr[x],arr[y]=arr[y],arr[x]
      if arr[0]=='0':
        continue
      arr = int(''.join(map(str,arr)))
      if arr not in check[num]:
        if num==k:
          ans = max(ans,arr)
          continue
        check[num].add(arr)


print(ans)
