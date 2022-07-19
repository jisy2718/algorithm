# 다익스트라 문제

n, m , r = map(int,input().split())

items = list(map(int,input().split()))

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int,input().split())
    graph[a][b] = l
    graph[b][a] = l


import heapq
INF = 0XFFFFFFF
def dijkstra(start):
    distance = [INF]*(n+1)
    heap = []
    heapq.heappush(heap,[0,start])
    distance[start] = 0

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        for next_node in range(1,n+1):
            next_dist = graph[cur_node][next_node]
            if next_dist > 0: # 현재노드와 이어진 길이 있다면
                next_dist = next_dist + cur_dist

                # 더 짧은 거리로 이동 가능하다면
                if next_dist < distance[next_node]:
                    distance[next_node] = next_dist
                    heapq.heappush(heap, [next_dist, next_node])
    return distance


# 전체 노드에서 다익스트라 돌아보며, 최대 개수 구하기
max_count = 0
for v in range(1,n+1):
    count = 0
    distance = dijkstra(v)
    for i in range(1,n+1):
        if distance[i] <= m:
            count += items[i-1]

    if max_count < count:
        max_count = count
print(max_count)