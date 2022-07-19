# N = int(input())
# M = int(input())
# arrL = [[] for _ in range(M)]
# for _ in range(M):
#     s, e, c = map(int,input().split())
#     arrL[s].append([e,c])
#
# s, e = map(int,input().split())
# INF = 0XFFFFFFFFFFFFFF
# cost = [INF]*(N+1)
#
# cost[s] = 0
# path = []
# path.append(s)
# for neighbor_cost in arrL[s]:
#     n, c = neighbor_cost
#     cost[n] = c
#
# min_idx = INF
# min_val = INF
#
# while min_idx != e:
#
#     # 최소인 곳으로 이동
#     for node in range(1,N+1):
#         if node not in path and cost[node] < min_val:
#             min_val = cost[node]
#             min_idx = node
#
#     path.append(min_idx)
#     print(path)
#
#     # 각 노드로의 이동 최소 비용 update
#
#     # 이동거리 업데이트
#     # 기존의 A->B > A->C 기존 + C->B NEW
#     for neighbor_cost in arrL[min_idx]:
#         n, c = neighbor_cost
#         if cost[n] > cost[min_idx] + c:
#             cost[n] = cost[min_idx] + c
#
#
# print(cost[e])
# print(len(path))
# print(*path)
#






import sys
input = sys.stdin.readline

V = int(input())
E = int(input())


arr = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())

    arr[u].append((v,w))
K, e = map(int,input().split())
visited = [0]*(V+1)
INF = 0XFFFFFFFFFFFFFFFF
cost = [INF]*(V+1)

# 시작점에서 최단거리 초기화
cost[K] = 0
visited[K] = 0
path = []
for node, weight in arr[K]:
    cost[node] = min(cost[node], weight)  # 중복 간선 있을 수 있으므로

    # visited set 이용하면 while(len(visited)<V) 로 진행 가능
for _ in range(V+1):

    # 가장 비용이 적은 곳 방문
    min_node = 0
    for node in range(1,V+1):
        if visited[node]==0 and cost[node] < cost[min_node] : # 방문 안한 곳중 최소비용찾기
            min_node = node

    visited[min_node] = 1
    path.append(min_node)
    # 방문한 곳에서 이동하는 비용과 현재 이동하는 비용 비교해서, 이동 비용 update
    for node, weight in arr[min_node]:
        # 현재 이동 비용 vs. 방문한 곳에서 이동비용
        cost[node] = min( cost[node], cost[min_node]  + weight)


print(*path)
