# N, M, X = map(int,input().split())
#
# INF = 0XFFFFFFFF
# arr = [[INF]*(N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     s, e, w = map(int,input().split())
#     arr[s][e] = w
#
# def dijk(s,e):
#
#     visited = set()
#
#     visited.add(s)
#     cost = arr[s].copy()
#     cost[s] = 0
#
#     while e not in visited:
#         # 최소 비용인 곳으로 이동
#         min_val = INF
#         min_idx = -1
#         for i in range(1,N+1):
#             if i not in visited and cost[i] < min_val:
#                 min_val = cost[i]
#                 min_idx = i
#
#
#
#         visited.add(min_idx)
#
#
#         # 이동한 곳에서 새로 이동 가능한 곳들 있다면, 최소비용 update
#         for i in range(1,N+1):
#             if i not in visited and arr[min_idx][i] != INF: # 방문하지 않았고, 이동 가능하면, 비용 비교
#                 # 기존 i 까지 비용 > 기존 min_idx 까지 비용 + arr[min_idx][i]
#                 if cost[i] > cost[min_idx] + arr[min_idx][i]:
#                     cost[i] = cost[min_idx] + arr[min_idx][i]
#
#     # print(f's and e is {s}, {e}, cost is {cost}')
#
#     return(cost[e])
#
#
#
# def dijk2(s):
#
#     visited = set()
#
#     visited.add(s)
#     cost = arr[s].copy()
#     cost[s] = 0
#
#     while len(visited)!=N:
#         # 최소 비용인 곳으로 이동
#         min_val = INF
#         min_idx = -1
#         for i in range(1,N+1):
#             if i not in visited and cost[i] < min_val:
#                 min_val = cost[i]
#                 min_idx = i
#
#
#
#         visited.add(min_idx)
#
#
#         # 이동한 곳에서 새로 이동 가능한 곳들 있다면, 최소비용 update
#         for i in range(1,N+1):
#             if i not in visited and arr[min_idx][i] != INF: # 방문하지 않았고, 이동 가능하면, 비용 비교
#                 # 기존 i 까지 비용 > 기존 min_idx 까지 비용 + arr[min_idx][i]
#                 if cost[i] > cost[min_idx] + arr[min_idx][i]:
#                     cost[i] = cost[min_idx] + arr[min_idx][i]
#
#     # print(f's and e is {s}, {e}, cost is {cost}')
#
#     return(cost)
#
#
# sol = [0]*(N+1)
# cost_X = dijk2(X)
# for s in range(1,N+1):
#     sol[s] += dijk(s,X)
#     sol[s] += cost_X[s]
#
# print(max(sol))




#
#
# n, M, X = map(int,input().split())
#
# INF = 0XFFFFFFFF
# distance = [[INF] * (n+1) for _ in range(n+1)]
# for _ in range(M):
#     a,b,c = map(int, input().split())
#     if distance[a][b] > c:
#         distance[a][b] = c
#
# for i in range(1, n+1): # 징검다리
#     for j in range(1, n+1): # 출발
#         for k in range(1, n+1): # 도착
#             if j != k:
#                 if distance[j][k] > distance[j][i] + distance[i][k]:
#                     distance[j][k] = distance[j][i] + distance[i][k]
#
#
# sol = distance[X].copy()  # X -> 모든 점까지의 거리
# sol[X] = 0
#
# # for i in range(1,n+1):
# #     if sol[i] == INF
# for s in range(1,n+1):
#     if s !=X:
#         sol[s] += distance[s][X]  # 모든 각 점에서 -> X까지의 거리
#
# print(max(sol[1:]))




#--------------------------------------------------------
import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(start_node):
    distance = [INF] * (N + 1)
    heap = []
    heapq.heappush(heap, [0, start_node])
    distance[start_node] = 0

    while heap:
        now_cost, node = heapq.heappop(heap)  # 현재 해당 node로 이동하는 비용, 해당 node

        for next_cost, next_node in arr[node]:  # 해당 node에서 next_node로 움직이는 비용
            next_cost = next_cost + now_cost

            if next_cost < distance[next_node]:  # 기존의 next_node 까지 이동하는 비용보다 작다면, update
                distance[next_node] = next_cost
                heapq.heappush(heap, [next_cost, next_node])  # 새로 이동한 곳을 heap에 넣기

    return distance


N, M, X = map(int, input().split())

arr = [[] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

answer = [0] * (N + 1)
arr2 = dijkstra(X)

for i in range(1, N + 1):
    arr1 = dijkstra(i)
    answer[i] += arr1[X]  # i에서 X로 가는 비용
    answer[i] += arr2[i]  # X에서 i로 가는 비용

print(max(answer))