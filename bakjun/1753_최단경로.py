


V, E = map(int,input().split())

K = int(input()) # 시작점

arr = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())

    arr[u].append((v,w))


visited = [0]*(V+1)
INF = 0XFFFFFFFFFFFFFFFF
cost = [INF]*(V+1)

# 시작점에서 최단거리 초기화
cost[K] = 0
visited[K] = 0
for node, weight in arr[K]:
    cost[node] = min(cost[node], weight)  # 중복 간선 있을 수 있으므로

for _ in range(V+1):

    # 가장 비용이 적은 곳 방문
    min_node = 0
    for node in range(1,V+1):
        if visited[node]==0 and cost[node] < cost[min_node] : # 방문 안한 곳중 최소비용찾기
            min_node = node

    visited[min_node] = 1
    # 방문한 곳에서 이동하는 비용과 현재 이동하는 비용 비교해서, 이동 비용 update
    for node, weight in arr[min_node]:
        # 현재 이동 비용 vs. 방문한 곳에서 이동비용
        cost[node] = min( cost[node], cost[min_node]  + weight)


for node in range(1,V+1):
    if cost[node] == INF:
        print("INF")
    else:
        print(cost[node])
