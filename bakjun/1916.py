# N = int(input())
# M = int(input())
#
# INF = 0XFFFFFFFF
# arr = [[INF]*(N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     s, e, w = map(int,input().split())
#     arr[s][e] = w
#
# s, e = map(int,input().split())
#
# visited = set()
#
# visited.add(s)
# cost = arr[s].copy()
# cost[s] = 0
#
# while e not in visited:
#     # 최소 비용인 곳으로 이동
#     min_val = INF
#     min_idx = -1
#     for i in range(1,N+1):
#         if i not in visited and cost[i] < min_val:
#             min_val = cost[i]
#             min_idx = i
#
#
#
#     visited.add(min_idx)
#
#
#     # 이동한 곳에서 새로 이동 가능한 곳들 있다면, 최소비용 update
#     for i in range(1,N+1):
#         if i not in visited and arr[min_idx][i] != INF: # 방문하지 않았고, 이동 가능하면, 비용 비교
#             # 기존 i 까지 비용 > 기존 min_idx 까지 비용 + arr[min_idx][i]
#             if cost[i] > cost[min_idx] + arr[min_idx][i]:
#                 cost[i] = cost[min_idx] + arr[min_idx][i]
#
# print(cost[e])
#


#----------------------------------
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start_node):
    distance = [INF] * (N+1)
    heap = []
    heapq.heappush(heap, [0, start_node])
    distance[start_node] = 0

    while heap:
        now_cost, node = heapq.heappop(heap) # 현재 해당 node로 이동하는 비용, 해당 node
        for next_cost, next_node in arr[node]: # 해당 node에서 next_node로 움직이는 비용
            next_cost = next_cost + now_cost

            if next_cost < distance[next_node]:  # 기존의 next_node 까지 이동하는 비용보다 작다면, update
                distance[next_node] = next_cost
                heapq.heappush(heap, [next_cost, next_node])  # 새로 이동한 곳을 heap에 넣기

    return distance

N = int(input())
M = int(input())

INF = 0XFFFFFFFF
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int,input().split())
    arr[s].append((c, e))

s, e = map(int,input().split())

cost = dijkstra(s)

print(cost[e])
