import sys
from collections import deque

sys.stdin = open('커리큘럼.txt')


T = int(input())
score = [0]*(T+1)
indegree = [0]*(T+1) #진입차수
graph=[[] for _ in range(T+1)]

for i in range(1,T+1):
    l = [*map(int,input().split())]
    score[i]=l[0]
    ll = l[1:-1]
    for j in range(len(ll)):
        indegree[i]+=1
        graph[ll[j]].append(i)

Q = deque()

#큐에 진입차수가 0인거 집어넣기
for i in range(1,len(indegree)):
    if indegree[i]==0:
        Q.append(i)

#연결도해야하고
# 차수도표시


print(score)
print(indegree)

