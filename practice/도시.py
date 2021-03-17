import sys
sys.stdin = open("input\\in_city.txt")

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
# N: 집갯수, M: 길갯수
parent = [x for x in range(N+1)]

edges = []
result = 0

for i in range(M):
    A, B, C = map(int, input().split()) # A, B: 집번호 C: 가중치
    edges.append([C, A, B])

# 크루스칼
# 가중치순으로 정렬
# 사이클확인
edges.sort()
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):#사이클이없을때
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result - last)